# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import math

import mcpi.block
from mcpi.vec3 import Vec3

from mcthings.block import Block
from .decorator import Decorator
from ..world import World


class BorderDecorator(Decorator):
    """
    A Border Decorator to build the border of the Thing.

    Create a border of 1 block around the Thing
    """

    margin = 5  # Margin between the Thing and its border

    @classmethod
    def decorate(cls, thing):
        """
        Add a border to the Thing

        :return:
        """

        width = thing.end_position.x - thing.position.x + cls.margin
        large = thing.end_position.z - thing.position.z + cls.margin

        init_pos = Vec3(thing.position.x - cls.margin, thing.position.y, thing.position.z - cls.margin)
        end_pos = Vec3(thing.position.x + cls.margin, thing.position.y, thing.position.z + cls.margin)

        # Create the four borders of the Thing
        # Block by block with pre-clean so railways work
        init = init_pos
        end = Vec3(init_pos.x + 2 * width, init_pos.y, init_pos.z)
        for x in range(0, 2 * width):
            World.server.setBlock(init.x + x, init.y, init.z, cls.block)

        init = end
        end = Vec3(init.x, init.y, init.z + 2 * large )
        for z in range(0, 2 * large):
            World.server.setBlock(init.x, init.y, init.z + z, cls.block)

        init = end
        end = Vec3(init.x - 2 * width, init.y, init.z)
        for x in range(0, 2 * width):
            World.server.setBlock(init.x - x, init.y, init.z, cls.block)

        init = end
        end = Vec3(init.x, init.y, init.z - 2 * large)
        for z in range(0, 2 * large):
            World.server.setBlock(init.x, init.y, init.z - z, cls.block)
