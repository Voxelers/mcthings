# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

# TODO: at some point this must be a real Singleton
import pickle

from mcpi.vec3 import Vec3

from mcthings.utils import build_schematic_nbt


class Scene:
    """
    A scene is a container for all the things built using McThings.
    A scene can be built, unbuilt and moved. There is only one scene
    in a program using McThings. Things built are added automatically to
    the Scene. A Scene can also be loaded from a file, and
    it can be saved to a file.

    Before adding Things to the Scene, it must be connected to a
    Minecraft server (fill the Scene.server attribute)
    """

    things = []
    """ map with the things in the scene"""
    server = None
    """ Minecraft server in which create things"""
    _position = None

    @classmethod
    def add(cls, thing):
        """ Add a new thing to the scene """
        if not cls.things:
            # The initial position of the scene is the position
            # of its first thing added
            cls._position = thing.position
        cls.things.append(thing)

    @classmethod
    def build(cls):
        """ Build all the things inside the Scene """
        for thing in cls.things:
            thing.build()

    @classmethod
    def unbuild(cls):
        """ Unbuild all the things inside the Scene """
        for thing in cls.things:
            thing.unbuild()

    @classmethod
    def reposition(cls, position):
        """
        Move all the things in the scene to a new relative position

        :param position: new position for the Scene
        :return:
        """

        # All the things inside the scene must be moved
        diff_x = position.x - cls._position.x
        diff_y = position.y - cls._position.y
        diff_z = position.z - cls._position.z

        for thing in cls.things:
            repos_x = thing.position.x + diff_x
            repos_y = thing.position.y + diff_y
            repos_z = thing.position.z + diff_z

            thing._position = (Vec3(repos_x, repos_y, repos_z))

    @classmethod
    def move(cls, position):
        """
        Move the scene to a new position

        :param position: new position
        :return:
        """

        cls.unbuild()
        cls.reposition(position)
        cls.build()

    @classmethod
    def load(cls, file_path):
        """ Load a scene from a file (but no build it yet) """
        Scene.things = pickle.load(open(file_path, "rb"))
        if Scene.things:
            Scene._position = Scene.things[0].position

    @classmethod
    def save(cls, file_path):
        """ Save a scene to a file """
        pickle.dump(Scene.things, open(file_path, "wb"))

    @classmethod
    def to_schematic(cls, file_path):
        """
        Save the Scene into a Schematic file

        :file_path: file in which to export the Scene in Schematic format
        :return: the Schematic object
        """

        # Default init values
        init_pos = Vec3(cls._position.x, cls._position.y, cls._position.z)
        end_pos = Vec3(cls._position.x, cls._position.y, cls._position.z)

        for thing in cls.things:
            ip = thing.position
            ep = thing.end_position

            # Update init position
            init_pos.x = ip.x if ip.x < init_pos.x else init_pos.x
            init_pos.y = ip.y if ip.y < init_pos.y else init_pos.y
            init_pos.z = ip.z if ip.z < init_pos.z else init_pos.z

            # Update end position
            end_pos.x = ep.x if ep.x > end_pos.x else end_pos.x
            end_pos.y = ep.y if ep.y > end_pos.y else end_pos.y
            end_pos.z = ep.z if ep.z > end_pos.z else end_pos.z

            build_schematic_nbt(init_pos, end_pos).write_file(file_path)
