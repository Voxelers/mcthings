#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import sys
import time

import mcpi.block
import mcpi.minecraft
from mcpi.vec3 import Vec3

from mcthings.bridge import Bridge
from mcthings.building import Building
from mcthings.fence import Fence
from mcthings.line import Line
from mcthings.pyramid import PyramidHollow
from mcthings.scene import Scene
from mcthings.river import River
from mcthings.schematic import Schematic
from mcthings.server import Server
from mcthings.sphere import SphereHollow
from mcthings.town import Town

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        server = Server(MC_SEVER_HOST, MC_SEVER_PORT)

        server.mc.postToChat("Building a Scene with several Things")
        pos = server.mc.entity.getTilePos(server.mc.getPlayerEntityId(BUILDER_NAME))
        pos.x += 1

        if False:
            # Load the Schematic to test it
            s = Schematic(Vec3(pos.x+20, pos.y, pos.z))
            s.file_path = "../schematics/scene0_30.schematic"
            s.build()
            s

        # Scene 0.10

        # River

        river_width = 10
        river = River(pos)
        river.width = river_width
        river.length = 100
        river.build()
        # time.sleep(5)

        # Bridges are created for crossing the river
        # Position them and 1/4 and 3/4 of the length of the river

        bridge_start = Bridge(Vec3(pos.x - 1, pos.y, pos.z + (river.length * (1 / 4))))
        bridge_start.height = 3
        bridge_start.large = river.width + 2
        bridge_start.width = 2
        bridge_start.block = mcpi.block.WOOD
        bridge_start.build()

        bridge_end = Bridge(Vec3(pos.x - 1, pos.y, pos.z + (river.length * (3 / 4))))
        bridge_end.height = 3
        bridge_end.large = river.width + 2
        bridge_end.width = 2
        bridge_end.block = mcpi.block.WOOD
        bridge_end.build()

        # Lines (paths) at both sides of the river

        line_width = 2
        line_right = Line(Vec3(pos.x - (3 + line_width), pos.y, pos.z))
        line_right.block = mcpi.block.SAND
        line_right.length = river.length
        line_right.width = line_width
        line_right.build()

        line_left = Line(Vec3(pos.x + river.width + 3, pos.y, pos.z))
        line_left.block = mcpi.block.SAND
        line_left.length = river.length
        line_left.width = line_width
        line_left.build()

        # Create the houses along the river

        house_width = 5
        house_length = 5
        houses = 4 * 3 + 1

        p = line_right.position
        # 2 line width
        town_right = Town(Vec3(p.x - 2, p.y, p.z))
        town_right.house_width = house_width
        town_right.house_length = house_length
        town_right.house_mirror = True
        town_right.houses = houses
        town_right.build()

        p = line_left.position
        # 2 line width
        town_left = Town(Vec3(p.x + (2 + 1), p.y, p.z))
        town_left.house_width = house_width
        town_left.house_length = house_length
        town_left.houses = houses
        town_left.build()

        # Create the Temple (Pyramid)

        temple_far = 30  # closer than the jail

        # First the path from the town to the temple
        p = line_right.position
        p_z = p.z + house_length + 1
        line_temple = Line(Vec3(p.x, p.y, p_z))
        line_temple.block = mcpi.block.SAND
        line_temple.width = -temple_far
        line_temple.length = 2
        line_temple.build()
        # And now the temple
        temple_height = 15
        temple_width = 2 * temple_height - 1

        p = line_temple.end_position
        p_z = p.z - temple_width / 2
        p_x = p.x - temple_width
        temple = PyramidHollow(Vec3(p_x, p.y, p_z))
        temple.height = temple_height
        temple.build()

        # Create the Jail (Fenced town)

        jail_far = 50
        fence_space = 5

        # First the path from the town to the jail
        p = line_left.position
        p_z = p.z + house_length + 1
        line_jail = Line(Vec3(p.x, p.y, p_z))
        line_jail.block = mcpi.block.SAND
        line_jail.width = +jail_far
        line_jail.length = 2
        line_jail.build()

        # The jail town
        house_jail_width = 10
        p = line_jail.end_position
        p_z = p.z - (2 * house_jail_width)
        p_x = p.x
        town_jail = Town(Vec3(p_x, p.y, p_z))
        town_jail.space = 1
        town_jail.house_width = house_jail_width
        town_jail.block = mcpi.block.STONE
        town_jail.build()

        fence_jail = Fence(None)
        fence_jail.thing = town_jail
        fence_jail.block = mcpi.block.BEDROCK
        fence_jail.fence_space = fence_space
        fence_jail.build()

        # buildings (group of buildings)

        building_far = 40

        # First the path from the town to the buildings
        p = line_right.end_position
        p_z = p.z - (house_length + 1)
        line_building = Line(Vec3(p.x, p.y, p_z))
        line_building.block = mcpi.block.SAND
        line_building.width = -building_far
        line_building.length = 2
        line_building.build()

        # Now the buildings
        building_width = 10
        p = line_building.end_position
        building1 = Building(Vec3(p.x, p.y, p.z - building_width / 2))
        building1.width = building_width
        building1.house_mirror = True
        building1.build()

        p_z = p.z - 2 * building_width
        building2 = Building(Vec3(p.x, p.y, p_z))
        building2.width = building_width
        building2.build()

        # Create the Stadium (sphere)
        stadium_far = 50

        # First the path from the town to the stadium
        p = line_left.end_position
        p_z = p.z - (house_length + 1)
        line_stadium = Line(Vec3(p.x, p.y, p_z))
        line_stadium.block = mcpi.block.SAND
        line_stadium.width = +stadium_far
        line_stadium.length = 2
        line_stadium.build()

        p = line_stadium.end_position
        radius = 15
        stadium = SphereHollow(Vec3(p.x - radius, p.y, p.z - radius))
        stadium.radius = radius
        stadium.block = mcpi.block.IRON_BLOCK
        stadium.build()

        # Save as Schematic
        Scene.to_schematic("../schematics/scene_0_30.schematic")

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
