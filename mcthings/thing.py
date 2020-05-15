# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import mcpi.block
import mcpi.vec3

from nbt.nbt import NBTFile, TAG_Float, TAG_SHORT, TAG_List, TAG_Int, TAG_Short, TAG_Byte_Array, TAG_Byte, TAG_String

from ._version import __version__

from .scene import Scene


class Thing:
    """ base class for all objects in mcthings library """

    block = mcpi.block.BRICK_BLOCK
    """ block type used by the thing. Default to BRICK_BLOCK"""
    _block_empty = mcpi.block.AIR

    def __init__(self, position):
        """
        Create a thing
        :param position: build position
        """

        self._end_position = None
        self._position = None
        if position:
            self._position = mcpi.vec3.Vec3(position.x, position.y, position.z)

        # Add then thing built to the scene
        Scene.add(self)

        # McThing version which created this Thing
        self._version = __version__

    @property
    def position(self):
        """ initial position of the thing """
        return self._position

    @property
    def end_position(self):
        """ end position of the thing """
        return self._end_position

    def build(self):
        """
        Build the thing and show it in Minecraft at position coordinates

        :return:
        """

    def unbuild(self):
        """
        Unbuild the thing in Minecraft

        :return:
        """

        block = self.block
        self.block = self._block_empty
        self.build()
        self.block = block

    def move(self, position):
        """
        Move the thing to a new position

        :param position: new position
        :return:
        """

        self.unbuild()
        self._position = position
        self.build()

    def to_schematic(self, file_path):
        """
        Convert the Thing to a Schematic Object

        :file_path: file in which to export the Thing in Schematic format
        :return: the Schematic object
        """

        size_x = self.end_position.x - self.position.x + 1
        size_z = self.end_position.z - self.position.z + 1
        size_y = self.end_position.y - self.position.y + 1

        # Prepare the NBT Object
        nbtfile = NBTFile()
        nbtfile.name = "Schematic"
        nbtfile.tags.append(TAG_Short(name="Width", value=size_x))
        nbtfile.tags.append(TAG_Short(name="Height", value=size_y))
        nbtfile.tags.append(TAG_Short(name="Length", value=size_z))
        nbt_blocks = TAG_Byte_Array(name="Blocks")
        nbtfile.tags.append(nbt_blocks)
        nbt_data = TAG_Byte_Array(name="Data")
        nbtfile.tags.append(nbt_data)

        # Additional fields need
        nbtfile.tags.append(TAG_String(name="Materials", value="Alpha"))
        nbtfile.tags.append(TAG_Int(name="'WEOriginX'", value=0))
        nbtfile.tags.append(TAG_Int(name="'WEOriginY'", value=0))
        nbtfile.tags.append(TAG_Int(name="'WEOriginZ'", value=0))
        nbtfile.tags.append(TAG_Int(name="'WEOffsetX'", value=0))
        nbtfile.tags.append(TAG_Int(name="'WEOffsetY'", value=0))
        nbtfile.tags.append(TAG_Int(name="'WEOffsetZ'", value=0))
        entities_list = TAG_List(name="Entities", type=TAG_Int)
        nbtfile.tags.append(entities_list)
        tile_entities_list = TAG_List(name="TileEntities", type=TAG_Int)
        nbtfile.tags.append(tile_entities_list)

        # Collect all blocks information a fill the NBT Data
        # Use the same loop than in Schematic format: x -> z -> y

        blocks_bytes = bytearray()
        data_bytes = bytearray()

        for y in range(0, size_y):
            for z in range(0, size_z):
                for x in range(0, size_x):
                    block_pos = mcpi.vec3.Vec3(self.position.x + x, self.position.y + y, self.position.z + z)
                    block = Scene.server.getBlockWithData(block_pos.x, block_pos.y, block_pos.z)
                    blocks_bytes.append(block.id)
                    data_bytes.append(block.data)

        nbt_blocks.value = blocks_bytes
        nbt_data.value = data_bytes

        nbtfile.write_file(file_path)
