#!/usr/bin/env python3

import logging
import unittest

from mcthings.blocks_gallery import BlocksGallery
from tests.base import TestBaseThing


class TestBlocksGallery(TestBaseThing):
    """Test  Thing"""

    def test_build(self):
        self.server.mc.postToChat("Building a blocks gallery with all available blocks")

        pos = self.pos

        pos.x += 1

        gallery = BlocksGallery(pos)
        gallery.build()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
