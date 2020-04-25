import sys

import mcpi.block
import mcpi.minecraft
from mcpi.vec3 import Vec3

from mcthings.line import Line
from mcthings.server import Server


BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        server = Server(MC_SEVER_HOST, MC_SEVER_PORT)

        server.mc.postToChat("Building a line")
        pos = server.mc.entity.getTilePos(server.mc.getPlayerEntityId(BUILDER_NAME))

        pos.x += 1
        line = Line(pos)
        line.width = 2
        line.block = mcpi.block.SAND
        line.length = 10
        line.width = 1
        line.build()

        line = Line(line.end_position)
        line.width = 2
        line.block = mcpi.block.STONE
        line.build()

        line = Line(line.end_position)
        line.length = 10
        line.width = 2
        line.block = mcpi.block.SAND
        line.build()

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
