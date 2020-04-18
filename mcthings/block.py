from .creation import Creation
from .thing import Thing


class Block(Thing):

    def build(self):
        Creation.server.setBlock(self.position.x, self.position.y,
                                 self.position.z, self.block)

        self._end_position = self.position
