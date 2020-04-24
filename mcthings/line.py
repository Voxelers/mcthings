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

        # Find the type of land block destroyed with the line
        self._block_empty = \
            Scene.server.getBlock(self.position.x, self.position.y-1, self.position.z)

        Scene.server.setBlocks(self.position.x, self.position.y-1, self.position.z,
                               end_x, end_y, end_z, self.block)

        self._end_position = Vec3(end_x, end_y + 1, end_z)

    # endpoint must be repositioned also
    def reposition(self, position):

        diff_x = position.x - self._position.x
        diff_z = position.z - self._position.z

        self._position = position
        self._end_position = None

        endpoint_x = self.end_point[0] + diff_x
        endpoint_z = self.end_point[1] + diff_z

        self.end_point = [endpoint_x, endpoint_z]
