# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import mcpi

from mcpi.vec3 import Vec3

from .thing import Thing


class House(Thing):

    height = 3
    width = 5
    length = 5
    wall_width = 1
    door_size = 1
    mirror = False

    def create(self):

        init_x = self.position.x
        init_y = self.position.y
        init_z = self.position.z

        end_x = init_x + self.length - 1
        if self.mirror:
            end_x = init_x
            init_x = init_x - (self.length - 1)
        end_y = init_y + self.height - 1
        end_z = init_z + self.width - 1

        self.set_blocks(
            Vec3(init_x, init_y, init_z),
            Vec3(end_x, end_y, end_z),
            self.block.id)

        # Fill the cube with air so it becomes a kind of house
        init_x_empty = init_x + self.wall_width
        end_x_empty = end_x - self.wall_width
        self.set_blocks(
            Vec3(init_x_empty, init_y, init_z + self.wall_width),
            Vec3(end_x_empty,
                 end_y - self.wall_width,
                 end_z - self.wall_width),
            mcpi.block.AIR.id)

        init_door_x = init_x
        if self.mirror:
            init_door_x = end_x
        init_door = Vec3(init_door_x, init_y, init_z + self.wall_width)
        end_door_x = init_door_x + self.wall_width - 1
        end_door_y = init_y + self.door_size
        end_door_z = init_z + self.wall_width + self.door_size - 1
        end_door = Vec3(end_door_x, end_door_y, end_door_z)
        self.set_blocks(init_door, end_door, mcpi.block.AIR.id)

        self._end_position = Vec3(end_x, end_y, end_z)
