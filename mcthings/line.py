from mcpi.vec3 import Vec3

from .scene import Scene
from .thing import Thing


class Line(Thing):

    width = 3
    length = 10
    end_point = None
    """ x,z coordinates"""

    def build(self):
        end_x = self.position.x + self.length - 1
        end_y = self.position.y - 1
        end_z = self.position.z + self.width - 1

        if self.end_point:
            end_x = self.end_point[0]
            end_z = self.end_point[1]

        Scene.server.setBlocks(self.position.x, self.position.y-1, self.position.z,
                               end_x, end_y, end_z, self.block)

        self._end_position = Vec3(end_x, end_y + 1, end_z)
