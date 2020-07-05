#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

from mcpi.vec3 import Vec3
from nbt import nbt

from mcthings.blocks import Blocks
from mcthings.blocks_memory import BlocksMemory, BlockMemory
from mcthings.collage import Collage
from mcthings.schematic import Schematic
from mcthings.vox import Vox


class TestBlocksMemory(unittest.TestCase):
    """Test BlocksMemory"""

    def test_create(self):
        pass

    # Add a test for all public methods at least

    def test_add_block(self):
        mem = BlocksMemory()
        mem.add(BlockMemory(0, 0, 0))
        assert len(mem.blocks) == 1

    def test_find_init_end_pos(self):
        alien = Schematic(Vec3(0, 0, 0))
        alien.file_path = "schematics/alien_engi1a.schematic"
        alien.create()

        init, end = alien.find_bounding_box()
        minit, mend = alien._blocks_memory.find_init_end_pos()

        assert init == minit
        assert end == mend

    def test_is_cuboid(self):

        blocks = Blocks(Vec3(0, 0,0))
        blocks.create()
        assert blocks._blocks_memory.is_cuboid()

        # The schematic from a not cuboid vox is exported as a cuboid
        alien = Schematic(Vec3(0, 0, 0))
        alien.file_path = "schematics/alien_engi1a.schematic"
        alien.create()

        assert alien._blocks_memory.is_cuboid()

        # The vox model is not a cuboid
        alien = Vox(Vec3(0, 0, 0))
        alien.file_path = "vox/alien_engi1a.vox"
        alien.create()

        assert not alien._blocks_memory.is_cuboid()

    def test_memory_equal(self):
        blocks = Blocks(Vec3(0, 0,0))
        blocks.create()
        assert blocks._blocks_memory.memory_equal()

        blocks = Collage(Vec3(0, 0,0))
        blocks.create()
        assert not blocks._blocks_memory.memory_equal()

    def test_flip_x(self):
        blocks = Blocks(Vec3(20, 0, 0))
        blocks.create()

        init_pos, end_pos = blocks._blocks_memory.find_init_end_pos()

        blocks.flip_x()
        finit_pos, fend_pos = blocks._blocks_memory.find_init_end_pos()

        assert finit_pos.x == init_pos.x - (blocks.width - 1)
        assert fend_pos.x == end_pos.x - (blocks.width - 1)

    def test_rotate(self):
        blocks = Blocks(Vec3(0, 0, 0))
        blocks.width = 2
        blocks.length = 3
        blocks.height = 2
        blocks.create()

        init_pos, end_pos = blocks._blocks_memory.find_init_end_pos()
        blocks_size = len(blocks._blocks_memory.blocks)

        """
        (1, 2, 1)
        **
        **
        *(*)
        (0, 0, 0)
        
        After 90 degrees rotation based on (*)
        (0, 1, 1)
        ***
        (*)**
        (-2 , 0, 0)
        """

        blocks.rotate(90)
        rot_init_pos, rot_end_pos = blocks._blocks_memory.find_init_end_pos()
        rot_blocks_size = len(blocks._blocks_memory.blocks)

        assert blocks_size == rot_blocks_size

        assert rot_init_pos == Vec3(-2, 0, 0)
        assert rot_end_pos == Vec3(0, 1, 1)

    def test_set_block(self):
        mem = BlocksMemory()
        mem.set_block(Vec3(1, 0, 0), 1, 0)
        mem.set_block(Vec3(0, 0, 0), 0, 0)
        assert len(mem.blocks) == 2
        assert mem.blocks[0].id == 1

    def test_set_blocks(self):
        mem = BlocksMemory()
        # 3 x 2 x 2 = 12 blocks
        blocks_end_position = Vec3(2, 1, 1)
        mem.set_blocks(Vec3(0, 0, 0), blocks_end_position, 0)
        assert len(mem.blocks) == 12

        init_pos, end_pos = mem.find_init_end_pos()

        assert end_pos == blocks_end_position
        assert mem.is_cuboid()

    def test_find_block_at_pos(self):
        mem = BlocksMemory()
        pos = Vec3(1, 2, 3)
        block_id = 40
        block_data = 15
        mem.set_block(pos, block_id, block_data)
        mem.set_block(Vec3(0, 0, 0), 0, 0)

        block = mem.find_block_at_pos(pos)
        assert block.id == block_id and block.data == block_data

    def test_memory_to_nbt(self):
        # Load a schematic and count the number of blocks in the NBT structure
        alien = Schematic(Vec3(0, 0, 0))
        alien.file_path = "schematics/alien_engi1a.schematic"
        alien_colors = 5
        alien.create()

        data = nbt.NBTFile(alien.file_path, 'rb')
        size_x = data["Width"].value
        size_y = data["Height"].value
        size_z = data["Length"].value
        expected_blocks = size_x * size_y * size_z

        blocks_bytes, data_bytes = alien._blocks_memory.to_nbt(alien.position, alien.end_position)

        assert len(blocks_bytes) == expected_blocks

        # Check the data reflects correctly the number of colors
        number_wool_colors = len(set(data_bytes))

        assert number_wool_colors == alien_colors


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
