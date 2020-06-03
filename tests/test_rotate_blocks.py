#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

from mcpi.vec3 import Vec3
import mcpi.block

from mcthings.blocks import Blocks
from mcthings.collage import Collage
from mcthings.world import World
from tests.base import TestBaseThing


class TestRotateBlock(TestBaseThing):
    """ Test to rotate Blocks """

    def test_build(self):
        World.server.postToChat("Building two blocks")

        pos = self.pos

        pos.x += 3
        blocks = Collage(pos)
        blocks.width = 7
        blocks.height = 2
        blocks.length = 3
        blocks.build()

        pos.x += 15
        blocks = Collage(pos)
        blocks.width = 7
        blocks.height = 2
        blocks.length = 3
        blocks.build()
        blocks.rotate(90)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
