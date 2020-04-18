import sys

import mcpi.block
import mcpi.minecraft


from mcthings.block import Block
from mcthings.creation import Creation

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        mc = mcpi.minecraft.Minecraft.create(address=MC_SEVER_HOST, port=MC_SEVER_PORT)
        Creation.server = mc

        mc.postToChat("Building a block")
        pos = mc.entity.getTilePos(mc.getPlayerEntityId(BUILDER_NAME))

        pos.x += 1
        block = Block(pos)
        block.build()

        pos.x += 3
        block = Block(pos)
        block.build()

        pos.y = +1
        Creation.move(pos)

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
