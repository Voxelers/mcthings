#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

from mcthings.blocks import Blocks
from mcthings.collage import Collage
from mcthings.world import World
from tests.base import TestBaseThing


class TestFlipBlock(TestBaseThing):
    """ Test to flip Blocks """

    def test_build(self):
        World.renderer.post_to_chat("Building two blocks")

        pos = self.pos

        pos.x += 3
        blocks = Collage(pos)
        blocks.width = 2
        blocks.height = 1
        blocks.length = 2
        blocks.create()
        blocks.render()

        pos.x += 6
        blocks = Collage(pos)
        blocks.width = 2
        blocks.height = 1
        blocks.length = 2
        blocks.create()
        blocks.flip_x()
        blocks.render()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
