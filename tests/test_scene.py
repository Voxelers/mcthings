#!/usr/bin/env python3

import logging
import unittest

from mcthings.block import Block
from mcthings.scene import Scene
from tests.base import TestBaseThing


class TestScene(TestBaseThing):
    """Test Scene Thing"""

    def test_build(self):
        self.server.mc.postToChat("Building a scene")

        pos = self.pos

        pos.x += 1
        block = Block(pos)
        block.build()

        pos.x += 2
        block = Block(pos)
        block.build()

        pos.y += 1
        Scene.move(pos)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
