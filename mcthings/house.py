import mcpi

from mcpi.vec3 import Vec3

from .thing import Thing


class House(Thing):

    height = 3
    width = 5
    length = 5
    wall_width = 1
    door_size = 1

    def build(self):
        init_x = self.position.x
        init_y = self.position.y
        init_z = self.position.z

        end_x = init_x + self.length-1
        end_y = init_y + self.height-1
        end_z = init_z + self.width-1

        self.server.setBlocks(
            init_x, init_y, init_z,
            end_x, end_y, end_z,
            self.block)

        # Fill the cube with air so it becomes a kind of house
        self.server.setBlocks(
            init_x + self.wall_width, init_y, init_z + self.wall_width,
            end_x - self.wall_width,
            end_y - self.wall_width,
            end_z - self.wall_width,
            mcpi.block.AIR)

        # Add a door
        self.server.setBlocks(
            init_x, init_y, init_z + self.wall_width,
            init_x + 1, init_y + self.door_size, init_z + self.door_size,
            mcpi.block.AIR)

        self._end_position = Vec3(end_x, end_y, end_z)


