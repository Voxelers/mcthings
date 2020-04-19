import sys

import mcpi.block
import mcpi.minecraft

from mcthings.scene import Scene
from mcthings.wall import Wall

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        mc = mcpi.minecraft.Minecraft.create(address=MC_SEVER_HOST, port=MC_SEVER_PORT)
        Scene.server = mc

        mc.postToChat("Building a wall")
        pos = mc.entity.getTilePos(mc.getPlayerEntityId(BUILDER_NAME))
        pos.x += 1

        wall = Wall(pos)
        wall.build()

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
