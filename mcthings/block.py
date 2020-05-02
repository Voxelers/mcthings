# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

from .scene import Scene
from .thing import Thing


class Block(Thing):

    def build(self):
        Scene.server.setBlock(self.position.x, self.position.y,
                              self.position.z, self.block)

        self._end_position = self.position
