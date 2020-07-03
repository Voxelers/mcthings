#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

from mcpi.vec3 import Vec3

from mcthings.utils import find_min_max_cuboid_vertex


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


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
