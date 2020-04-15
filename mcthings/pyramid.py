from mcpi.vec3 import Vec3


from .thing import Thing


class Pyramid(Thing):

    height = 10

    def build(self):
        length = 2 * self.height - 1
        width = length

        for i in range(0, self.height):
            level = i
            self.server.setBlocks(
                self.position.x + level, self.position.y + level, self.position.z + level,
                self.position.x + (length - 1) - level,
                self.position.y + level,
                self.position.z + (width - 1) - level,
                self.block)

        self._end_position = Vec3(self.position.x + (length - 1),
                                  self.position.y + self.height,
                                  self.position.z + (width - 1)
                                  )
