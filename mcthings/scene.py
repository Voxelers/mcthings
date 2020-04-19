# TODO: at some point this must be a real Singleton
import pickle

from mcpi.vec3 import Vec3


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
        """ Recover all the map building the things"""
        for thing in cls.things:
            thing.build()

    @classmethod
    def unbuild(cls):
        """ Recover all the map unbuilding the things """
        for thing in cls.things:
            thing.unbuild()

    @classmethod
    def move(cls, position):
        """
        Move the scene to a new position

        :param position: new position
        :return:
        """

        # All the things inside the scene must be moved
        diff_x = position.x - cls._position.x
        diff_y = position.y - cls._position.y
        diff_z = position.z - cls._position.z

        for thing in Scene.things:
            move_x = thing.position.x + diff_x
            move_y = thing.position.y + diff_y
            move_z = thing.position.z + diff_z

            thing.move(Vec3(move_x, move_y, move_z))

    @classmethod
    def load(cls, file_path):
        """ Load a scene from a file """
        Scene.things = pickle.load(open(file_path, "rb"))
        Scene._position = Scene.things[0].position

    @classmethod
    def save(cls, file_path):
        """ Save a scene to a file """
        pickle.dump(Scene.things, open(file_path, "wb"))


