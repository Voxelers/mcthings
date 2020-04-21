import sys

import mcpi.block
import mcpi.minecraft

from mcthings.scene import Scene
from mcthings.server import Server
from minecraftstuff import MinecraftDrawing

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        server = Server(MC_SEVER_HOST, MC_SEVER_PORT)
        scene_path = "scene_sphere_drawing.mct"

        server.mc.postToChat("Cleaning a scene")

        # Let's load the scene and build it
        Scene.load(scene_path)
        # Move the scene to the player position
        Scene.unbuild()

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
