import sys

import mcpi.block
import mcpi.minecraft

from mcthings.bridge import Bridge
from mcthings.house import House
from mcthings.river import River


BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        mc = mcpi.minecraft.Minecraft.create(address=MC_SEVER_HOST, port=MC_SEVER_PORT)

        mc.postToChat("Building a scene")
        pos = mc.entity.getTilePos(mc.getPlayerEntityId(BUILDER_NAME))
        pos.x += 1

        river_width = 10
        house_to_river = 5
        house_width = 5

        house = House(mc, pos)
        house.mirror = True
        house.width = house_width
        house.build()

        # Create a river between the houses

        pos.x += house_to_river + 1
        river = River(mc, pos)
        river.width = river_width
        river.build()

        # Create a bridge over the river
        pos.x -= 1
        bridge = Bridge(mc, pos)
        bridge.large = river_width + 2
        bridge.block = mcpi.block.STONE
        bridge.build()

        pos.x = river.end_position.x + 1 + house_to_river
        house = House(mc, pos)
        house.width = house_width
        house.build()

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
