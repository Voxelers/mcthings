from math import floor

from mcpi.vec3 import Vec3

from .thing import Thing


class Bridge(Thing):

    large = 5

    def build(self):
        # large = 2 * self.height - 1
        max_height = floor((self.large + 1) / 2)

        for x in range(0, self.large):
            if x < max_height:
                y = x
            elif x == max_height and self.large % 2 == 0:
                y = x - 1
            else:
                y = y - 1
            self.server.setBlock(
                self.position.x + x, self.position.y + y, self.position.z,
                self.block)

        self._end_position = Vec3(self.position.x + self.large - 1,
                                  self.position.y,
                                  self.position.z
                                  )
