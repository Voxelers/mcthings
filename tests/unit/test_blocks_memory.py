#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

from mcpi.vec3 import Vec3

from mcthings.vox import Vox


class TestBlocksMemory(unittest.TestCase):
    """Test BlocksMemory"""

    def test_create(self):
        pass

    # Add a test for all public methods at least



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
