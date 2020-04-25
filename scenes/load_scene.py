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
        scene_path = "scene_sphere_drawing.mct"

        server.mc.postToChat("Building a scene from " + scene_path)
        pos = server.mc.entity.getTilePos(server.mc.getPlayerEntityId(BUILDER_NAME))
        pos.z += 10

        # Let's load the scene and build it
        Scene.load(scene_path)
        # Position the scene to the player position
        Scene.reposition(pos)
        Scene.build()

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
