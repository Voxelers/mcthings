# TODO: at some point this must be a real Singleton

from mcpi.minecraft import Minecraft
# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import mcpi.block


class Decorator:
    """
    A Decorator is able to decorate a Thing based on its characteristics.

    If a Thing has decorators, they will be called after the build of the Thing.
    """

    block = mcpi.block.AIR
    """ Base block for the decorator """

    @classmethod
    def decorate(cls, thing):
        """
        Decorate the thing

        :return:
        """
