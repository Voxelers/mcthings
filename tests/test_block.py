#!/usr/bin/env python3

import logging
import unittest

from mcpi.vec3 import Vec3

from mcthings.block import Block
from tests.base import TestBaseThing


class TestBlock(TestBaseThing):
    """Test Block Thing"""

    def test_build(self):
        self.server.mc.postToChat("Building two blocks")

        pos = self.pos

        pos.x += 1
        block = Block(pos)
        block.build()

        pos.x += 3
        block = Block(pos)
        block.build()
        block.unbuild()

        block.move(Vec3(pos.x+5, pos.y, pos.z))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
