import sys

import mcpi.block
import mcpi.minecraft

from mcthings.fence import Fence
from mcthings.pyramid import Pyramid
from mcthings.server import Server
from mcthings.town import Town

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        server = Server(MC_SEVER_HOST, MC_SEVER_PORT)

        server.mc.postToChat("Building a walled town")
        pos = server.mc.entity.getTilePos(server.mc.getPlayerEntityId(BUILDER_NAME))
        pos.x += 10

        town = Town(pos)
        town.houses = 3
        town.block = mcpi.block.WOOD
        town.house_width = 10
        town.house_length = 10
        town.house_height = 10
        town.build()

        # Build the wall to round the town
        fence = Fence()
        fence.block = mcpi.block.GOLD_BLOCK
        fence.thing = town
        fence.thick = 4
        fence.height = 10
        fence.build()

        pos.x += 30
        pyr = Pyramid(pos)
        pyr.build()
        fence = Fence()
        fence.thing = pyr
        fence.build()

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
