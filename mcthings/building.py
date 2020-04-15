import mcpi

from .thing import Thing
from .house import House


class Building(Thing):

    floors = 10
    width = 10

    def build(self):
        init_x = self.position.x
        init_y = self.position.y
        init_z = self.position.z

        house_pos = mcpi.vec3.Vec3(init_x, init_y, init_z)
        init_height = init_y

        for i in range(0, self.floors):
            house = House(self.server, house_pos)
            house_pos.y = house.height * i + init_height
            house.width = self.width
            house.block = self.block
            house.build()
            self._end_position = house.end_position
