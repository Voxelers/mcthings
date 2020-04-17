import mcpi.block
from mcpi.vec3 import Vec3

from .thing import Thing


class River(Thing):

    length = 100
    width = 2
    depth = 1

    def build(self):
        init_x = self.position.x
        init_y = self.position.y - self.depth
        init_z = self.position.z

        end_x = init_x + self.width - 1
        end_y = self.position.y - 1
        end_z = init_z + self.length - 1

        self.server.setBlocks(
            init_x, init_y, init_z,
            end_x, end_y, end_z,
            mcpi.block.WATER_FLOWING)

        self._end_position = Vec3(end_x, end_y + self.depth, end_z)
