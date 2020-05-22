#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

import mcpi.block

from mcthings.block import Block
from mcthings.tower import Tower
from tests.base import TestBaseThing


class TestTower(TestBaseThing):
    """Test Tower Thing"""

    def test_build(self):
        self.server.mc. postToChat("Building a tower")

        self.pos.z += 1
        tower = Tower(self.pos)
        tower.top_size = 7
        tower.height = 5
        tower.build()

        block = Block(tower.end_position)
        block.block = mcpi.block.BEDROCK
        block.build()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
