from .object import Object


class Block(Object):

    def build(self):
        self.server.setBlock(self.position.x, self.position.y,
                             self.position.z, self.block)
