import sys

import mcpi.block
import mcpi.minecraft


from mcthings.bridge import Bridge

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        mc = mcpi.minecraft.Minecraft.create(address=MC_SEVER_HOST, port=MC_SEVER_PORT)

        mc.postToChat("Building a bridges")
        pos = mc.entity.getTilePos(mc.getPlayerEntityId(BUILDER_NAME))
        pos.x += 1

        bridge = Bridge(mc, pos)
        bridge.build()
        pos = bridge.end_position
        pos.x += 1
        bridge1 = Bridge(mc, pos)
        bridge1.block = mcpi.block.BEDROCK
        bridge1.build()

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
