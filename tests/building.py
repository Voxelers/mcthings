import sys

import mcpi.block
import mcpi.minecraft

from mcthings.building import Building
from mcthings.creation import Creation

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        mc = mcpi.minecraft.Minecraft.create(address=MC_SEVER_HOST, port=MC_SEVER_PORT)
        Creation.server = mc

        mc.postToChat("Building a building")
        pos = mc.entity.getTilePos(mc.getPlayerEntityId(BUILDER_NAME))

        building = Building(pos)
        building.block = mcpi.block.BEDROCK
        building.build()

        Building(building.end_position).build()

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
