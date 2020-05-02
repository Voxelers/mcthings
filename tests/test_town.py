#!/usr/bin/env python3

import logging
import unittest

import mcpi
from mcpi.vec3 import Vec3

from mcthings.town import Town
from tests.base import TestBaseThing


class TestTown(TestBaseThing):
    """Test Town Thing"""

    def test_build(self):
        self.server.mc.postToChat("Building a town")

        pos = self.pos

        pos.x += 1

        town = Town(pos)
        town.block = mcpi.block.BEDROCK
        town.build()

        town = Town(Vec3(pos.x-5, pos.y, pos.z))
        town.block = mcpi.block.BEDROCK
        town.house_mirror = True
        town.build()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
