#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

import mcpi.entity

from mcpi.vec3 import Vec3

from mcthings.entity import Entity
from mcthings.pyramid import PyramidHollow
from tests.base import TestBaseThing


class TestEntity(TestBaseThing):
    """ Test Entities """

    def test_spawn(self):
        self.server.mc.postToChat("Spawning entities in Minecraft")

        pos = self.pos

        # pos.x += 1
        # entity = Entity(pos)
        # entity.spawn()

        # # Let's create a pyramid so we can spawn entities inside
        # pos.x += 30
        # pyr = PyramidHollow(pos)
        # pyr.height = 20
        # pyr.build()

        # Let's create a dragon
        pos.x -= 2
        entity = Entity(pos)
        entity.entity = mcpi.entity.GIANT
        entity.spawn()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
