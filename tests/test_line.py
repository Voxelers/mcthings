import logging
import unittest

import mcpi

from mcthings.line import Line
from tests.base import TestBaseThing


class TestLine(TestBaseThing):
    """Test Line Thing"""

    def test_build(self):
        self.server.mc.postToChat("Building a line")

        pos = self.pos

        pos.x += 1
        line = Line(pos)
        line.width = 2
        line.block = mcpi.block.SAND
        line.length = 10
        line.width = 1
        line.build()

        line = Line(line.end_position)
        line.width = 2
        line.block = mcpi.block.STONE
        line.build()

        line = Line(line.end_position)
        line.length = 10
        line.width = 2
        line.block = mcpi.block.SAND
        line.build()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
