#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

from mcthings.schematic import Schematic
from tests.base import TestBaseThing


class TestSchematic(TestBaseThing):
    """Test Schematic Thing"""

    def test_build(self):

        self.server.mc.postToChat("Building a schematic")
        pos = self.pos

        schematic = Schematic(pos)
        # 2012: https://www.minecraft-schematics.com/schematic/68/
        # schematic.file_path = "schematics/pirate-boat.schematic"
        # 2017: https://www.minecraft-schematics.com/schematic/9676/
        # schematic.file_path = "schematics/chateau-fairmont.schematic"
        # schematic.file_path = "schematics/pyramid_hollow.schematic"
        schematic.file_path = "schematics/zanabot.schematic"
        schematic.build()
        schematic.to_schematic("schematics/zanabot-exported.schematic", blocks_data=False)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
