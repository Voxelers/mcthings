import sys

import mcpi.block
import mcpi.minecraft

from mcthings.scene import Scene
from mcthings.pyramid import Pyramid
from mcthings.server import Server

from mcthings.circle import Circle
from mcthings.sphere import Sphere

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        server = Server(MC_SEVER_HOST, MC_SEVER_PORT)

        server.mc.postToChat("Building the Sphere, Circle and Pyramid scene")
        pos = server.mc.entity.getTilePos(server.mc.getPlayerEntityId(BUILDER_NAME))
        init_y = pos.y
        init_x = pos.x

        radius = 10
        pos.z += 20

        circle = Circle(pos)
        circle.radius = radius
        circle.block = mcpi.block.BEDROCK
        circle.build()

        pos.y += round(radius/2) - 1
        sphere = Sphere(pos)
        sphere.radius = round(radius/2)
        sphere.block = mcpi.block.IRON_BLOCK
        sphere.build()

        pyr_height = 4
        pyr_width = (2 * pyr_height - 1)
        pos.x = init_x + round(radius/2)
        pos.y = init_y
        pyr = Pyramid(pos)
        pyr.height = 4
        pyr.block = mcpi.block.GOLD_BLOCK
        pyr.build()

        pos.x = init_x - round(radius/2) - pyr_width + 1
        pyr = Pyramid(pos)
        pyr.height = 4
        pyr.block = mcpi.block.GOLD_BLOCK
        pyr.build()

        Scene.save("scene_sphere_drawing.mct")

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
