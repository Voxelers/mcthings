import sys

import mcpi.block
import mcpi.minecraft


from mcthings.blocks import Blocks
from mcthings.scene import Scene
from mcthings.server import Server


BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        server = Server(MC_SEVER_HOST, MC_SEVER_PORT)

        server.mc.postToChat("Building blocks")
        pos = server.mc.entity.getTilePos(server.mc.getPlayerEntityId(BUILDER_NAME))

        pos.z += 1
        blocks = Blocks(pos)
        blocks.build()

        pos.z += 10
        blocks = Blocks(pos)
        blocks.build()

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
