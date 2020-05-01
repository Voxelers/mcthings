import logging
import unittest

import mcpi

from mcthings.building import Building
from tests.base import TestBaseThing


class TestBuilding(TestBaseThing):
    """Test Building Thing"""

    def test_build(self):
        self.server.mc.postToChat("Building a building")

        pos = self.pos

        pos.x += 1

        building = Building(pos)
        building.block = mcpi.block.BEDROCK
        building.house_mirror = True
        building.build()

        Building(building.end_position).build()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
