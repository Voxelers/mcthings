# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import sys
import unittest

import mcpi

from mcthings.server import Server


class TestBaseThing(unittest.TestCase):
    """ Integration tests for McThings """

    BUILDER_NAME = "ElasticExplorer"

    MC_SEVER_HOST = "localhost"
    MC_SEVER_PORT = 4711

    @classmethod
    def setUpClass(cls):
        try:
            cls.server = Server(cls.MC_SEVER_HOST, cls.MC_SEVER_PORT)
            cls.pos = cls.server.mc.entity.getTilePos(cls.server.mc.getPlayerEntityId(cls.BUILDER_NAME))

        except mcpi.connection.RequestError:
            logging.error("Can't connect to Minecraft server " + cls.MC_SEVER_HOST)
            sys.exit(1)

    def setUp(self):
        self.pos = self.server.mc.entity.getTilePos(self.server.mc.getPlayerEntityId(self.BUILDER_NAME))

