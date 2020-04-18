import sys

import mcpi.block
import mcpi.minecraft

from mcthings.bridge import Bridge
from mcthings.creation import Creation
from mcthings.house import House
from mcthings.river import River


BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        mc = mcpi.minecraft.Minecraft.create(address=MC_SEVER_HOST, port=MC_SEVER_PORT)
        Creation.server = mc

        mc.postToChat("Building a creation from a file")
        pos = mc.entity.getTilePos(mc.getPlayerEntityId(BUILDER_NAME))
        pos.x += 1

        # Let's load the creation and build it
        Creation.load("creation.p")
        creation_pos = Creation.things[0].position
        mc.postToChat("Initial position %s %s %s" % (creation_pos.x, creation_pos.y, creation_pos.z))
        Creation.build()

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
