import sys

import mcpi.block
import mcpi.minecraft

from mcthings.scene import Scene
from mcthings.server import Server

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        server = Server(MC_SEVER_HOST, MC_SEVER_PORT)

        server.mc.postToChat("Building a scene from a file")
        pos = server.mc.entity.getTilePos(server.mc.getPlayerEntityId(BUILDER_NAME))
        pos.x += 1

        # Let's load the scene and build it
        Scene.load("scene.mct")
        # Move the scene to the player position
        Scene.move(pos)
        Scene.build()

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
