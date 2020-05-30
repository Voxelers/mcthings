# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author/s (©): Alvaro del Castillo

from nbt import nbt

from mcpi.vec3 import Vec3

from mcthings.thing import Thing
from mcthings.world import World


class Schematic(Thing):
    _blocks_field = 'Blocks'
    _data_field = 'Data'
    file_path = None
    """ file path for the schematic file """

    def build(self):
        mc = World.server

        if not self.file_path:
            RuntimeError("Missing file_path param")

        schematic = nbt.NBTFile(self.file_path, 'rb')

        size_x = schematic["Width"].value
        size_y = schematic["Height"].value
        size_z = schematic["Length"].value

        init_x = self.position.x
        init_y = self.position.y
        init_z = self.position.z

        blocks = schematic[self._blocks_field]
        data = schematic[self._data_field]

        for y in range(0, size_y):
            for z in range(0, size_z):
                for x in range(0, size_x):
                    i = x + size_x * z + (size_x * size_z) * y
                    b = blocks[i]
                    if b != 0:
                        if self.block == self._block_empty:
                            # Cleaning the schematic
                            b = 0
                        d = data[i] & 0b00001111  # lower 4 bits
                        mc.setBlock(init_x + x, init_y + y, init_z + z, b, d)

        self._end_position = Vec3(init_x + size_x,
                                  init_y + size_y,
                                  init_z + size_z)
