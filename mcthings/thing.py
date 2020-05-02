# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import mcpi.block
import mcpi.vec3


class Thing:
    """ base class for all objects in mcthings library """

    block = mcpi.block.BRICK_BLOCK
    """ block type used by the thing. Default to BRICK_BLOCK"""
    _block_empty = mcpi.block.AIR

    def __init__(self, position):
        """
        Create a thing
        :param position: build position
        """

        self._end_position = None
        self._position = None
        if position:
            self._position = mcpi.vec3.Vec3(position.x, position.y, position.z)

        # Add then thing built to the scene
        from .scene import Scene

        Scene.add(self)

    @property
    def position(self):
        """ initial position of the thing """
        return self._position

    @property
    def end_position(self):
        """ end position of the thing """
        return self._end_position

    def build(self):
        """
        Build the thing and show it in Minecraft at position coordinates

        :return:
        """

    def unbuild(self):
        """
        Unbuild the thing in Minecraft

        :return:
        """

        block = self.block
        self.block = self._block_empty
        self.build()
        self.block = block

    def move(self, position):
        """
        Move the thing to a new position

        :param position: new position
        :return:
        """

        self.unbuild()
        self._position = position
        self.build()
