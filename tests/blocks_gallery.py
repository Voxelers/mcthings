import sys

import mcpi.block
import mcpi.minecraft

from mcthings.building import Building
from mcthings.blocks_gallery import BlocksGallery

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        mc = mcpi.minecraft.Minecraft.create(address=MC_SEVER_HOST, port=MC_SEVER_PORT)

        mc.postToChat("Building a blocks gallery with all available blocks")
        pos = mc.entity.getTilePos(mc.getPlayerEntityId(BUILDER_NAME))

        blocks = BlocksGallery(mc, pos)
        blocks.build()
        Building(mc, blocks.end_position).build()


    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
