import logging
import unittest

from mcthings.river import River
from tests.base import TestBaseThing


class TestRiver(TestBaseThing):
    """Test River Thing"""

    def test_build(self):
        self.server.mc.postToChat("Building a river")

        pos = self.pos

        pos.x += 1

        river = River(pos)
        river.width = 3
        river.depth = 3
        river.length = 5
        river.build()
        river.unbuild()

        river = River(river.end_position)
        river.depth = 3
        river.build()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
