# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo
import logging
import math

from mcpi.vec3 import Vec3
import mcpi.block

from mcthings.utils import size_region, find_min_max_cuboid_vertex


class BlockMemory:

    def __init__(self, block_id, block_data, pos):
        self.id = block_id
        self.data = block_data
        self.pos = pos


class BlocksMemory:
    """
    Blocks memory for a Thing
    """

    def __init__(self):

        self.blocks = []
        self._blocks_pos = {}

    def add(self, block_memory):
        """
        Add a new block to the memory.

        :param block_memory: memory for a block
        :return:
        """

        self.blocks.append(block_memory)

    def find_init_end_pos(self):
        """ Find the init and end cuboid positions from all the blocks in the memory """

        first_pos = self.blocks[0].pos

        init_pos = Vec3(first_pos.x, first_pos.y, first_pos.z)
        end_pos = Vec3(first_pos.x, first_pos.y, first_pos.z)

        for block in self.blocks:
            pos = block.pos
            if pos.x < init_pos.x:
                init_pos = Vec3(pos.x, init_pos.y, init_pos.z)
            if pos.y < init_pos.y:
                init_pos = Vec3(init_pos.x, pos.y, init_pos.z)
            if pos.z < init_pos.z:
                init_pos = Vec3(init_pos.x, init_pos.y, pos.z)

            if pos.x > end_pos.x:
                end_pos = Vec3(pos.x, end_pos.y, end_pos.z)
            if pos.y > end_pos.y:
                end_pos = Vec3(end_pos.x, pos.y, end_pos.z)
            if pos.z > end_pos.z:
                end_pos = Vec3(end_pos.x, end_pos.y, pos.z)

        return init_pos, end_pos

    def is_cuboid(self):
        """ Check if the memory is a filled cuboid """

        cuboid = False

        # Check that the number of blocks needed for the filled cuboid is the same that the blocks
        init_pos, vertex_max = self.find_init_end_pos()
        size = size_region(init_pos, vertex_max)

        if size.x * size.y * size.z == len(self.blocks):
            cuboid = True

        return cuboid

    def memory_equal(self):
        """ Check if all the blocks in the memory are equal """
        equal = True

        if self.blocks:
            last_block = self.blocks[0]

            for block in self.blocks:
                if block.id != last_block.id or block.data != last_block.data:
                    equal = False
                    break
                last_block = block
        else:
            equal = False

        return equal

    def flip_x(self, position):
        """
        Flip based on x-axis the blocks in memory using position as base position from which to rotate
        :param position: base position from which to rotate
        :return:
        """

        for block in self.blocks:
            # Find the x position and flip it
            width = abs(block.pos.x - position.x)
            # TODO: the flip could be done in two directions (left or right)
            # This one the the flip to the right
            x_flipped = position.x - width
            block.pos.x = x_flipped

    def fill(self, fill_block):
        """
        Fill all blocks in memory with fill_block

        :param fill_block: block to be used to fill all memory
        :return:
        """

        for block in self.blocks:
            block.id = fill_block.id
            block.data = fill_block.data

    def rotate(self, degrees, position):
        """
        Rotate degrees the blocks in memory using position as base position from which to rotate
        :param degrees: degrees to rotate (90, 180, 270)
        :param position: base position from which to rotate
        :return:
        """
        valid_degrees = [90, 180, 270]

        if degrees not in [90, 180, 270]:
            raise RuntimeError("Invalid degrees: %s (valid: %s) " % (degrees, valid_degrees))

        cos_degrees = math.cos(math.radians(degrees))
        sin_degrees = math.sin(math.radians(degrees))

        def rotate_x(pos_x, pos_z):
            return pos_x * cos_degrees - pos_z * sin_degrees

        def rotate_z(pos_x, pos_z):
            return pos_z * cos_degrees + pos_x * sin_degrees

        # Base position for the rotation
        init_pos = position
        rotated_blocks = []

        # Rotate all blocks with respect the initial position and add them
        for block in self.blocks:
            b = block.id
            d = block.data

            x = block.pos.x - init_pos.x
            z = block.pos.z - init_pos.z
            rotated_x = round(init_pos.x + rotate_x(x, z))
            rotated_z = round(init_pos.z + rotate_z(x, z))
            rotated_blocks.append(BlockMemory(b, d, Vec3(rotated_x, block.pos.y, rotated_z)))

        # Replace all blocks in memory with the rotated ones
        self.blocks = []
        for rotated_block in rotated_blocks:
            self.set_block(rotated_block.pos, rotated_block.id, rotated_block.data)

    def set_block(self, pos, block_id, block_data=None):
        self.add(BlockMemory(block_id, block_data, pos))

    def set_blocks(self, vertex, vertex_opposite, block_id):
        """ Add a cuboid with the same block for all blocks and without specific data """

        block_data = None

        width = abs(vertex_opposite.x - vertex.x) + 1
        height = abs(vertex_opposite.y - vertex.y) + 1
        length = abs(vertex_opposite.z - vertex.z) + 1

        vertex_min, vertex_max = find_min_max_cuboid_vertex(vertex, vertex_opposite)

        for y in range(0, height):
            for z in range(0, length):
                for x in range(0, width):
                    block_pos = Vec3(vertex_min.x + x, vertex_min.y + y, vertex_min.z + z)
                    self.set_block(block_pos, block_id, block_data)

    def _create_blocks_pos(self):
        logging.info("Creating the memory cache with positions")
        for block in self.blocks:
            self._blocks_pos[str(block.pos)] = block
        logging.info("Done memory cache with positions")

    def find_block_at_pos(self, pos):
        """
        Find a block in memory give its position
        TODO: Improve performance

        :param pos: position for the block
        :return: the block found or None
        """

        if not self._blocks_pos:
            self._create_blocks_pos()

        block_found = None
        if str(pos) in self._blocks_pos:
            block_found = self._blocks_pos[str(pos)]

        return block_found

    def to_nbt(self, init_pos, end_pos):
        """
        Convert the blocks of memory to NBT format for exporting as Schematic
        The NBT must be a complete cuboid with air in the positions where
        there are no data in blocks memory.


        :return: bytearrays for blocks ids and block data
        """

        size = size_region(init_pos, end_pos)

        blocks_bytes = bytearray()
        data_bytes = bytearray()

        # Use the same loop than reading Schematic format: x -> z -> y
        for y in range(0, size.y):
            for z in range(0, size.z):
                for x in range(0, size.x):
                    block_data = 0
                    block_id = mcpi.block.AIR.id
                    block_pos = Vec3(init_pos.x + x, init_pos.y + y, init_pos.z + z)
                    # Find if there is a block at block_pos
                    mem_block = self.find_block_at_pos(block_pos)
                    if mem_block:
                        block_id = mem_block.id
                        block_data = mem_block.data
                    blocks_bytes.append(block_id)
                    data_bytes.append(block_data)

        return blocks_bytes, data_bytes

    def build_schematic(self):
        init_pos, end_pos = self.find_init_end_pos()

        return self.to_nbt(init_pos, end_pos, self)

    def to_schematic(self, file_path):
        """
        Convert the blocks memory to a Schematic Object

        :file_path: file in which to export the memory in Schematic format
        :return: the Schematic object
        """

        self.build_schematic().write_file(file_path)

