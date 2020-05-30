# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import mcpi.block
from mcpi.vec3 import Vec3

from .thing import Thing
from .world import World


class River(Thing):

    length = 100
    width = 2
    depth = 1
    block = mcpi.block.WATER_FLOWING

    def build(self):

        init_x = self.position.x
        init_y = self.position.y - self.depth
        init_z = self.position.z

        end_x = init_x + self.width - 1
        end_y = self.position.y - 1
        end_z = init_z + self.length - 1

        # Find the type of land block destroyed with the river
        self._block_empty = \
            World.server.getBlock(init_x, self.position.y - 1, init_z)

        World.server.setBlocks(
            init_x, init_y, init_z,
            end_x, end_y, end_z,
            self.block)

        self._end_position = Vec3(end_x, self.position.y - self.depth, end_z)
