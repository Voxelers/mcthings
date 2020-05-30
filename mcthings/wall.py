# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

from .world import World
from .thing import Thing


class Wall(Thing):
    height = 5
    length = 10
    width = 2

    def build(self):

        World.server.setBlocks(
            self.position.x, self.position.y, self.position.z,
            self.position.x+self.length-1,
            self.position.y+self.height-1,
            self.position.z+self.width-1,
            self.block)
