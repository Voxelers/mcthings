#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo
import logging
import sys
import time

import mcpi.block
import mcpi.minecraft
from mcpi.vec3 import Vec3

from mcthings.block import Block
from mcthings.bridge import Bridge
from mcthings.building import Building
from mcthings.fence import Fence
from mcthings.line import Line
from mcthings.platform import Platform
from mcthings.pyramid import PyramidHollow
from mcthings.scene import Scene
from mcthings.river import River
from mcthings.server import Server
from mcthings.sphere import SphereHollow
from mcthings.thing import Thing
from mcthings.town import Town

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711
EVENTS_PER_CLICK = 3
CHECK_EVENTS_TIME = 2


class SceneInteractive:
    """
    Scene Interactive

    The player will build the complete Scene interacting with the build command HQ.
    In this HQ the player can build the next Thing in scene, unbuilt the current one
    and go to the previous one, or she can modify the properties of the active Thing.

    The full scene is built complete hidden and then we play with it interacting.
    """

    # Common data for the Scene for relative positioning
    house_length = None
    line_left = None
    line_right = None
    line_width = 2
    pos = None
    river = None
    bridge_start = None
    bridge_end = None
    paths = None
    houses = None
    temple = None
    jail = None
    buildings = None
    stadium = None
    active_thing = 0

    @classmethod
    def move_step(cls, forward=True):

        if forward:
            if cls.active_thing + 1 < len(Scene.things):
                cls.active_thing += 1
        else:
            if cls.active_thing > 0:
                cls.active_thing -= 1

        return Scene.things[cls.active_thing]

    @classmethod
    def build_river(cls):
        river_width = 10
        river = River(cls.pos)
        cls.river = river
        river.width = river_width
        river.length = 100
        river.build()

    @classmethod
    def build_bridges(cls):

        # Bridges are created for crossing the river
        # Position them and 1/4 and 3/4 of the length of the river
        pos = cls.pos
        river = cls.river

        bridge_start = Bridge(Vec3(pos.x - 1, pos.y, pos.z + (river.length * (1 / 4))))
        cls.bridge_start = bridge_start
        bridge_start.height = 3
        bridge_start.large = river.width + 2
        bridge_start.width = 2
        bridge_start.block = mcpi.block.WOOD
        bridge_start.build()

        bridge_end = Bridge(Vec3(pos.x - 1, pos.y, pos.z + (river.length * (3 / 4))))
        cls.bridge_end = bridge_end
        bridge_end.height = 3
        bridge_end.large = river.width + 2
        bridge_end.width = 2
        bridge_end.block = mcpi.block.WOOD
        bridge_end.build()

    @classmethod
    def build_paths(cls):

        # Lines (paths) at both sides of the river
        pos = cls.pos
        river = cls.river

        line_right = Line(Vec3(pos.x - (3 + cls.line_width), pos.y, pos.z))
        cls.line_right = line_right
        line_right.block = mcpi.block.SAND
        line_right.length = river.length
        line_right.width = cls.line_width
        line_right.build()

        line_left = Line(Vec3(pos.x + river.width + 3, pos.y, pos.z))
        cls.line_left = line_left
        line_left.block = mcpi.block.SAND
        line_left.length = river.length
        line_left.width = cls.line_width
        line_left.build()

    @classmethod
    def build_houses(cls):
        # Create the houses along the river

        house_width = 5
        house_length = 5
        cls.house_length = house_length
        houses = 4 * 3 + 1

        p = cls.line_right.position
        town_right = Town(Vec3(p.x - cls.line_width, p.y, p.z))
        town_right.house_width = house_width
        town_right.house_length = house_length
        town_right.house_mirror = True
        town_right.houses = houses
        town_right.build()

        p = cls.line_left.position
        town_left = Town(Vec3(p.x + (cls.line_width + 1), p.y, p.z))
        town_left.house_width = house_width
        town_left.house_length = house_length
        town_left.houses = houses
        town_left.build()

    @classmethod
    def build_temple(cls):

        # Create the Temple (Pyramid)

        temple_far = 30  # closer than the jail

        # First the path from the town to the temple
        p = cls.line_right.position
        p_z = p.z + cls.house_length + 1
        line_temple = Line(Vec3(p.x - (cls.line_width - 1), p.y, p_z))
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

    @classmethod
    def build_jail(cls):
        # Create the Jail (Fenced town)

        jail_far = 50
        fence_space = 5

        # First the path from the town to the jail
        p = cls.line_left.position
        p_z = p.z + cls.house_length + 1
        line_jail = Line(Vec3(p.x + cls.line_width, p.y, p_z))
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

    @classmethod
    def build_buildings(cls):

        # buildings (group of buildings)

        building_far = 40

        # First the path from the town to the buildings
        p = cls.line_right.end_position
        p_z = p.z - (cls.house_length + 1)
        line_building = Line(Vec3(p.x - cls.line_width, p.y, p_z))
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

    @classmethod
    def build_stadium(cls):

        # Create the Stadium (sphere)
        stadium_far = 50

        # First the path from the town to the stadium
        p = cls.line_left.end_position
        p_z = p.z - (cls.house_length + 1)
        line_stadium = Line(Vec3(p.x + (cls.line_width - 1), p.y, p_z))
        line_stadium.block = mcpi.block.SAND
        line_stadium.width =+ stadium_far
        line_stadium.length = 2
        line_stadium.build()

        p = line_stadium.end_position
        radius = 15
        stadium = SphereHollow(Vec3(p.x - radius, p.y, p.z - radius))
        stadium.radius = radius
        stadium.block = mcpi.block.IRON_BLOCK
        stadium.build()

    @classmethod
    def prepare_scene(cls):
        cls.build_river()
        cls.build_bridges()
        cls.build_paths()
        cls.build_houses()
        cls.build_temple()
        cls.build_jail()
        cls.build_buildings()
        cls.build_stadium()

        # Hide the scene to show it with the interactive tools
        Scene.unbuild()

    @classmethod
    def main(cls):
        try:
            server = Server(MC_SEVER_HOST, MC_SEVER_PORT)

            server.mc.postToChat("Building an Interactive Scene")
            cls.pos = server.mc.entity.getTilePos(server.mc.getPlayerEntityId(BUILDER_NAME))
            cls.pos.x += 1

            mc = server.mc
            entity_id = mc.getPlayerEntityId(BUILDER_NAME)
            mc.entity.getPos(entity_id)

            top_size = 5
            platform = Platform(Vec3(cls.pos.x, cls.pos.y, cls.pos.z-25))
            platform.block = mcpi.block.GLASS
            platform.height = 10
            platform.top_size = top_size

            cls.prepare_scene()

            platform.build()

            # Put the player in the platform
            p = platform.end_position
            player_pos = Vec3(p.x, p.y + 1, p.z - 4)
            server.mc.entity.setTilePos(server.mc.getPlayerEntityId(BUILDER_NAME), player_pos)

            # Put a blocks over the platform to change the block type to be used
            block = Block(Vec3(player_pos.x - (top_size - 1),
                               player_pos.y,
                               player_pos.z + (top_size - 1))
                          )
            block.block = mcpi.block.BEDROCK
            block.build()

            block = Block(Vec3(player_pos.x - (top_size/2 - 1),
                               player_pos.y,
                               player_pos.z + (top_size - 1))
                          )
            block.block = mcpi.block.GLASS
            block.build()

            block = Block(Vec3(player_pos.x,
                               player_pos.y,
                               player_pos.z + (top_size - 1))
                          )
            block.block = mcpi.block.BRICK_BLOCK
            block.build()

            while True:
                hits = mc.events.pollBlockHits()
                if len(hits) > EVENTS_PER_CLICK:
                    # Unbuild the current step and select the previous one
                    # Except the platform
                    if cls.active_thing > 0:
                        thing = Scene.things[cls.active_thing]
                        logging.info("Unbuilt" + str(thing))
                        thing.unbuild()
                    cls.move_step(forward=False)
                elif len(hits) > 0:
                    thing = cls.move_step()
                    logging.info("Moved to thing and build" + str(thing))
                    #  Get the block hit
                    hit = hits[0]
                    block_hit = server.mc.getBlock(hit.pos.x, hit.pos.y, hit.pos.z)
                    if block_hit != mcpi.block.GLASS.id:
                        build_block = thing.block
                        thing.block = block_hit
                        thing.build()
                        # Preserve the original block to restore it
                        thing.block = build_block
                    else:
                        thing.build()
                else:
                    thing = Scene.things[cls.active_thing]
                    logging.info("No actions. In " + str(thing))
                time.sleep(CHECK_EVENTS_TIME)

        except mcpi.connection.RequestError:
            print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    SceneInteractive.main()
    sys.exit(0)
