import sys

import mcpi.block
import mcpi.minecraft

from mcthings.creation import Creation
from mcthings.river import River

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        mc = mcpi.minecraft.Minecraft.create(address=MC_SEVER_HOST, port=MC_SEVER_PORT)
        Creation.server = mc

        mc.postToChat("Building a river")
        pos = mc.entity.getTilePos(mc.getPlayerEntityId(BUILDER_NAME))
        pos.x += 1

        river = River(pos)
        river.width = 3
        river.depth = 3
        river.build()

        river = River(river.end_position)
        river.depth = 3
        river.build()



    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
