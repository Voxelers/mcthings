#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

from mcpi.vec3 import Vec3

from mcthings.vox import Vox


class TestSchematic(unittest.TestCase):
    """Test Schematic Thing"""

    def test_create(self):

        # Old format
        vox = Vox(Vec3(0, 0 ,0))
        vox.file_path = "vox/alien_engi1a.vox"
        vox.create()

        # Old format with default palette
        vox = Vox(Vec3(0, 0 ,0))
        vox.file_path = "vox/chr_beardo3-default-palette.schematic"
        vox.create()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
