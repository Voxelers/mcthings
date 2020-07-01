#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

import mcpi.block
from mcpi.vec3 import Vec3

from mcthings.schematic import Schematic
from mcthings.world import World
from tests.base import TestBaseThing


class TestSchematic(TestBaseThing):
    """Test Schematic Thing"""

    def test_build(self):
        World.renderer.post_to_chat("Loading and building a schematic")
        pos = self.pos

        schematic = Schematic(pos)
        # 2012: https://www.minecraft-schematics.com/schematic/68/
        schematic.file_path = "schematics/pirate-boat.schematic"
        # 2017: https://www.minecraft-schematics.com/schematic/9676/
        # schematic.file_path = "schematics/chateau-fairmont.schematic"
        # schematic.file_path = "schematics/pyramid_hollow.schematic"
        schematic.change_blocks = {mcpi.block.ICE.id: mcpi.block.GLASS.id}
        schematic.file_path = "schematics/vxs.schematic"
        schematic.build()

        schematic = Schematic(Vec3(pos.x+4, pos.y, pos.z))
        schematic.file_path = "vox/vxs.schematic"
        schematic.build()

        schematic = Schematic(Vec3(pos.x+10, pos.y, pos.z))
        schematic.file_path = "vox/veh_ambulance_mc.schematic"
        schematic.build()

        schematic = Schematic(Vec3(pos.x+30, pos.y, pos.z))
        schematic.file_path = "schematics/obj_house6.schematic"
        schematic.build()




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
