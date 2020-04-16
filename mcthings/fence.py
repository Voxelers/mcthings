import mcpi

from .thing import Thing
from .wall import Wall


class Fence(Thing):
    """
    Build a block plane and empty it to create the fence
    """

    height = 3
    fence_space = 5
    """Space between the fence and the thing fenced"""
    thick = 1
    thing = None

    def build(self):

        if self.thing is None:
            raise RuntimeError("Thing to be fenced is not defined")

        self._position = self.thing.position
        self._end_position = self.thing.end_position

        init_x = self.thing.position.x - self.fence_space - self.thick
        init_y = self.thing.position.y
        init_z = self.thing.position.z - self.fence_space - self.thick

        end_x = self.thing.end_position.x + self.fence_space + self.thick
        end_y = self.thing.end_position.y
        end_z = self.thing.end_position.z + self.fence_space + self.thick

        self.server.setBlocks(
            init_x, init_y, init_z,
            end_x, end_y, end_z,
            self.block)

        # Fill the prism with air to became a rectangular wall
        self.server.setBlocks(
            init_x + self.thick, init_y, init_z + self.thick,
            end_x - self.thick,
            end_y,
            end_z - self.thick,
            mcpi.block.AIR)

        # Rebuild the thing because it is destroyed when emptying the fence
        self.thing.build()
