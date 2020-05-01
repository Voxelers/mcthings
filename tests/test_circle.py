import logging
import unittest

import mcpi

from mcthings.circle import Circle
from tests.base import TestBaseThing


class TestCircle(TestBaseThing):
    """Test Circle Thing"""

    def test_build(self):
        self.server.mc.postToChat("Building a circle")

        pos = self.pos

        radius = 10
        pos.z += 20

        circle = Circle(pos)
        circle.radius = radius
        circle.block = mcpi.block.BEDROCK
        circle.build()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
