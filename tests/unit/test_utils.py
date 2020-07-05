#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

from mcpi.vec3 import Vec3
from nbt import nbt

from mcthings.blocks import Blocks
from mcthings.schematic import Schematic
from mcthings.utils import find_min_max_cuboid_vertex, size_region


class TestUtils(unittest.TestCase):
    """ Test for the utils library """

    def test_cuboid_vertexes(self):
        # Find cuboid vertexes
        v1 = Vec3(1, 1, 0)
        v2 = Vec3(0, 1, 1)
        v_min, v_max = find_min_max_cuboid_vertex(v1, v2)

        assert v_min == Vec3(0, 1, 0)
        assert v_max == Vec3(1, 1, 1)

        v1 = Vec3(1, 0, 0)
        v2 = Vec3(0, 1, 1)
        v_min, v_max = find_min_max_cuboid_vertex(v1, v2)

        assert v_min == Vec3(0, 0, 0)
        assert v_max == Vec3(1, 1, 1)

    def test_size_region(self):
        # Load a schematic file with a know size and check this method
        schematic = Schematic(Vec3(0, 0, 0))
        schematic.file_path = "schematics/alien_engi1a.schematic"
        schematic.create()
        size = size_region(schematic.position, schematic.end_position)

        data = nbt.NBTFile(schematic.file_path, 'rb')
        size_x = data["Width"].value
        size_y = data["Height"].value
        size_z = data["Length"].value
        expected_size = Vec3(size_x, size_y, size_z)  # wrong +1 addition

        assert expected_size == size

        # Let's check with blocks also
        blocks = Blocks(Vec3(0, 0, 0))
        blocks.length = 5
        blocks.width = 5
        blocks.height = 5
        expected_size = Vec3(5, 5, 5)
        blocks.create()
        size = size_region(blocks.position, blocks.end_position)
        assert expected_size == size


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
