# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author/s (©): Alvaro del Castillo
import math

import mcpi
from nbt import nbt

from mcpi.vec3 import Vec3

from mcthings.thing import Thing
from mcthings.world import World


class Schematic(Thing):
    _blocks_field = 'Blocks'
    _data_field = 'Data'
    file_path = None
    """ file path for the schematic file """
    rotate_degrees = 0
    """ rotate the schematic """

    def find_bounding_box(self):
        """ In a Schematic the bounding box is inside the file data """

        schematic = nbt.NBTFile(self.file_path, 'rb')

        size_x = schematic["Width"].value
        size_y = schematic["Height"].value
        size_z = schematic["Length"].value

        init_x = self.position.x
        init_y = self.position.y
        init_z = self.position.z

        self._end_position = Vec3(init_x + size_x,
                                  init_y + size_y,
                                  init_z + size_z)

        return self.position, self.end_position

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

        cos_degrees = math.cos(math.radians(self.rotate_degrees))
        sin_degrees = math.sin(math.radians(self.rotate_degrees))

        def rotate_x(pos_x, pos_z):
            return pos_x * cos_degrees - pos_z * sin_degrees

        def rotate_z(pos_x, pos_z):
            return pos_z * cos_degrees + pos_x * sin_degrees

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

                        if self.rotate_degrees != 0:
                            rotated_x = init_x + rotate_x(x, z)
                            rotated_z = init_z + rotate_z(x, z)
                            World.server.setBlock(rotated_x, init_y + y, rotated_z, b, d)
                            self._end_position = mcpi.vec3.Vec3(rotated_x, init_y + y, rotated_z)
                        else:
                            mc.setBlock(init_x + x, init_y + y, init_z + z, b, d)
                            self._end_position = mcpi.vec3.Vec3(init_x + x, init_y + y, init_z + z)

    def rotate(self, degrees):
        """
        Rotate the thing in the x,z space. Blocks data is not preserved.

        In a Schematic, we load the data in memory, rotate it and build it

        :param degrees: degrees to rotate (90, 180, 270)
        :return:
        """

        valid_degrees = [90, 180, 270]

        if degrees not in [90, 180, 270]:
            raise RuntimeError("Invalid degrees: %s (valid: %s) " % (degrees, valid_degrees))

        self.rotate_degrees = degrees

        self.build()
