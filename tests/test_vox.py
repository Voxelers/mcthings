#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

from mcpi.vec3 import Vec3

from base import TestBaseThing
from mcthings.vox import Vox
from mcthings.world import World


class TestVox(TestBaseThing):
    """Test Vox Thing"""

    def test_build(self):

        # New format vox
        vox = Vox(self.pos)
        vox.file_path = "vox/vxs.vox"
        vox.create()
        vox.render()
        World.first_scene().to_schematic("schematics/vxs.schematic", True)

        # Old format vox
        vox = Vox(Vec3(self.pos.x + 10, self.pos.y, self.pos.z))
        vox.file_path = "vox/alien_engi1a.vox"
        vox.create()
        vox.render()

        # Old format vox converted to new one with MV
        vox = Vox(Vec3(self.pos.x + 30, self.pos.y, self.pos.z))
        vox.file_path = "vox/veh_ambulance_mc.vox"
        vox.create()
        vox.render()

        # Wool colors wall
        vox = Vox(Vec3(self.pos.x + 5, self.pos.y, self.pos.z + 10))
        vox.file_path = "vox/minecraft_wool.vox"
        vox.create()
        vox.flip_x()
        vox.render()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
