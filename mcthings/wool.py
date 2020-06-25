# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import mcpi

from mcpi.vec3 import Vec3
import mcpi.block

from .thing import Thing


class Wool(Thing):
    # Wool colors
    COLORS = [
        "White",
        "Orange",
        "Magenta",
        "Light Blue",
        "Yellow",
        "Lime",
        "Pink",
        "Grey",
        "Light grey",
        "Cyan",
        "Purple",
        "Blue",
        "Brown",
        "Green",
        "Red",
        "Black"
    ]

    def create(self):
        """
        Show all wool colors
        :return:
        """

        for i in range(0, len(self.COLORS)):
            p = self.position
            self.set_block(Vec3(p.x + i, p.y, p.z), mcpi.block.WOOL.id, i)

        self._end_position = Vec3(p.x + len(self.COLORS) - 1, p.y, p.z)
