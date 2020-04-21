import sys

import mcpi.block
import mcpi.minecraft

from mcthings.server import Server

from mcthings.sphere import Sphere

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711

# In this scene Things from McThings and McThings-Drawing are mixed


def main():
    try:
        server = Server(MC_SEVER_HOST, MC_SEVER_PORT)

        server.mc.postToChat("Building a sphere")
        pos = server.mc.entity.getTilePos(server.mc.getPlayerEntityId(BUILDER_NAME))

        radius = 10
        pos.z += 20

        pos.y += round(radius/2) - 1
        sphere = Sphere(pos)
        sphere.radius = round(radius/2)
        sphere.block = mcpi.block.IRON_BLOCK
        sphere.build()

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
