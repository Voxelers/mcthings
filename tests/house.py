import sys

import mcpi.block
import mcpi.minecraft

from mcthings.house import House
from mcthings.river import River


BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        mc = mcpi.minecraft.Minecraft.create(address=MC_SEVER_HOST, port=MC_SEVER_PORT)

        mc.postToChat("Building a house")
        pos = mc.entity.getTilePos(mc.getPlayerEntityId(BUILDER_NAME))
        pos.x += 1

        house = House(mc, pos)
        house.build()

        # Create a river between the houses
        pos.x -= 5
        river = River(mc, pos)
        river.build()

        # Mirror house
        pos.x -= 5 + river.width  # space between both houses
        house = House(mc, pos)
        house.mirror = True
        house.build()

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
