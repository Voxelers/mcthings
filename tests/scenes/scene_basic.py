#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import sys

import mcpi.block
import mcpi.minecraft

from mcthings.bridge import Bridge
from mcthings.scene import Scene
from mcthings.house import House
from mcthings.river import River
from mcthings.server import Server

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        server = Server(MC_SEVER_HOST, MC_SEVER_PORT)

        server.mc.postToChat("Building a Scene with several Things")
        pos = server.mc.entity.getTilePos(server.mc.getPlayerEntityId(BUILDER_NAME))
        pos.x += 1

        river_width = 10
        house_to_river = 5
        house_width = 5

        house = House(pos)
        house.mirror = True
        house.width = house_width
        house.build()

        # Create a river between the houses
        pos.x += house_to_river + 1
        river = River(pos)
        river.width = river_width
        river.build()

        # Create a bridge over the river
        pos.x -= 1
        bridge = Bridge(pos)
        bridge.large = river_width + 2
        bridge.block = mcpi.block.STONE
        bridge.build()

        pos.x = river.end_position.x + 1 + house_to_river
        house = House(pos)
        house.width = house_width
        house.build()

        # Let's persist the scene
        Scene.save("scene_basic.mct")

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
