import logging
import unittest


from mcthings.house import House
from tests.base import TestBaseThing


class TestHouse(TestBaseThing):
    """Test House Thing"""

    def test_build(self):
        self.server.mc.postToChat("Building a house")

        pos = self.pos

        pos.x += 1

        house = House(pos)
        house.build()

        # Mirror house
        pos.x -= 10   # space between both houses
        house = House(pos)
        house.mirror = True
        house.build()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
