from .object import Object


class Pyramid(Object):

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
