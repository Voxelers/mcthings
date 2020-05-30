#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

from mcpi.vec3 import Vec3

from mcthings.blocks import Blocks
from mcthings.world import World
from tests.base import TestBaseThing


class TestBlocks(TestBaseThing):
    """Test Blocks Thing"""

    def test_build(self):
        World.server.postToChat("Building blocks")

        self.pos.z += 1
        blocks = Blocks(self.pos)
        blocks.build()

        self.pos.z += 10
        blocks = Blocks(self.pos)
        blocks.build()

        blocks.move(Vec3(self.pos.x+5, self.pos.y, self.pos.z))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
