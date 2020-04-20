import sys

import mcpi.block
import mcpi.minecraft


from mcthings.bridge import Bridge
from mcthings.server import Server

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        server = Server(MC_SEVER_HOST, MC_SEVER_PORT)

        server.mc.postToChat("Building bridges")
        pos = server.mc.entity.getTilePos(server.mc.getPlayerEntityId(BUILDER_NAME))
        pos.x += 1

        bridge = Bridge(pos)
        bridge.build()
        pos = bridge.end_position
        pos.x += 1
        bridge1 = Bridge(pos)
        bridge1.block = mcpi.block.BEDROCK
        bridge1.build()

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
