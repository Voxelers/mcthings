import logging
import unittest

import mcpi

from mcthings.bridge import Bridge
from tests.base import TestBaseThing


class TestBridge(TestBaseThing):
    """Test Bridge Thing"""

    def test_build(self):
        self.server.mc.postToChat("Building bridges")

        pos = self.pos

        bridge = Bridge(pos)
        bridge.large = 10
        bridge.height = 3
        bridge.width = 3
        bridge.block = mcpi.block.WOOD
        bridge.build()

        pos = bridge.end_position
        pos.x += 1
        bridge1 = Bridge(pos)
        bridge1.large = 10
        bridge1.block = mcpi.block.BEDROCK
        bridge1.build()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
