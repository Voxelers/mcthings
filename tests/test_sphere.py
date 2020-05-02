#!/usr/bin/env python3

import logging
import unittest

import mcpi

from mcthings.sphere import Sphere
from mcthings.sphere import SphereHollow
from tests.base import TestBaseThing


class TestSphere(TestBaseThing):
    """Test Sphere Thing"""

    def test_build(self):
        self.server.mc.postToChat("Building a sphere")

        pos = self.pos

        radius = 10
        pos.z += 20

        pos.y += radius - 1
        sphere = Sphere(pos)
        sphere.radius = radius
        sphere.block = mcpi.block.IRON_BLOCK
        sphere.build()

        self.server.mc.postToChat("Building a hollow sphere")
        pos.x += 20
        sphere = SphereHollow(pos)
        sphere.radius = radius
        sphere.block = mcpi.block.WOOD
        sphere.build()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
