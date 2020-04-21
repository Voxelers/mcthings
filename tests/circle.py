import sys

import mcpi.block
import mcpi.minecraft

from mcthings.server import Server

from mcthings.circle import Circle

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711

# In this scene Things from McThings and McThings-Drawing are mixed


def main():
    try:
        server = Server(MC_SEVER_HOST, MC_SEVER_PORT)

        server.mc.postToChat("Building a circle")
        pos = server.mc.entity.getTilePos(server.mc.getPlayerEntityId(BUILDER_NAME))

        radius = 10
        pos.z += 20

        circle = Circle(pos)
        circle.radius = radius
        circle.block = mcpi.block.BEDROCK
        circle.build()

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
