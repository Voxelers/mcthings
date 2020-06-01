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

        (min_pos, max_pos) = thing.find_bounding_box()

        border_width = (max_pos.x - min_pos.x) + 1 + 2 * cls.margin + 2 * 1
        border_large = (max_pos.z - min_pos.z) + 1 + 2 * cls.margin + 2 * 1

        init_pos = Vec3(min_pos.x - (cls.margin + 1), min_pos.y, min_pos.z - (cls.margin + 1))
        end_pos = Vec3(min_pos.x + (cls.margin + 1), min_pos.y, min_pos.z + (cls.margin + 1))

        # Create the four borders of the Thing
        # Block by block with pre-clean so railways work
        init = init_pos
        end = Vec3(init_pos.x + border_width - 1, init_pos.y, init_pos.z)
        for x in range(0, border_width - 1):
            World.server.setBlock(init.x + x, init.y, init.z, cls.block)

        init = end
        end = Vec3(init.x, init.y, init.z + border_large - 1)
        for z in range(0, border_large - 1):
            World.server.setBlock(init.x, init.y, init.z + z, cls.block)

        init = end
        end = Vec3(init.x - (border_width - 1), init.y, init.z)
        for x in range(0, border_width - 1):
            World.server.setBlock(init.x - x, init.y, init.z, cls.block)

        init = end
        end = Vec3(init.x, init.y, init.z - (border_large - 1))
        for z in range(0, border_large - 1):
            World.server.setBlock(init.x, init.y, init.z - z, cls.block)
