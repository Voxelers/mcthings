# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import mcpi

from mcpi.vec3 import Vec3

from .thing import Thing
from .world import World


class BlocksGallery(Thing):

    # https://www.minecraftinfo.com/idlist.htm
    MAX_BLOCK_NUMBER = 247

    def build(self):
        """
        Show all possible block types in a line
        :return:
        """

        for i in range(1, self.MAX_BLOCK_NUMBER):
            World.server.setBlock(self.position.x + i, self.position.y,
                                  self.position.z, mcpi.block.Block(i))

        self._end_position = Vec3(self.position.x + self.MAX_BLOCK_NUMBER - 1,
                                  self.position.y, self.position.z)
