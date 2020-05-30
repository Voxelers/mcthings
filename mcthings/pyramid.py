# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import mcpi.block
from mcpi.vec3 import Vec3

from .thing import Thing
from .world import World


class Pyramid(Thing):

    height = 10

    def build(self):

        length = 2 * self.height - 1
        width = length

        for i in range(0, self.height):
            level = i
            World.server.setBlocks(
                self.position.x + level, self.position.y + level, self.position.z + level,
                self.position.x + (length - 1) - level,
                self.position.y + level,
                self.position.z + (width - 1) - level,
                self.block)

        self._end_position = Vec3(self.position.x + (length - 1),
                                  self.position.y + self.height - 1,
                                  self.position.z + (width - 1)
                                  )


class PyramidHollow(Thing):

    height = 10
    thick = 2

    def build(self):
        outer = Pyramid(self.position, self)
        outer.height = self.height
        outer.block = self.block
        outer.build()
        self._end_position = outer.end_position
        inner_x = self.position.x + self.thick
        inner_y = self.position.y
        inner_z = self.position.z + self.thick
        inner = Pyramid(Vec3(inner_x, inner_y, inner_z), self)
        inner.block = mcpi.block.AIR
        inner.height = self.height - self.thick
        inner.build()

