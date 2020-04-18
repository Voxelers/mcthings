# TODO: at some point this must be a real Singleton
import pickle

from mcpi.vec3 import Vec3


class Creation:
    """
    A creation is a container for all the things built using McThings.
    It can be used to unbuild or build a complete creation. The things
    data will be added during the construction, and it the future it will
    be loaded from a file or other kind of data storage.

    Before adding Things to the Creation, it must be connected to a
    Minecrfat server (fill the Creation.server attribute)
    """

    things = []
    """ map with the things in the creation"""
    server = None
    """ Minecraft server in which create things"""
    _position = None

    @classmethod
    def add(cls, thing):
        """ Add a new thing to the creation """
        if not cls.things:
            # The initial position of the creation is the position
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
        Move the creation to a new position

        :param position: new position
        :return:
        """

        # All the things inside the creation must be moved
        diff_x = position.x - cls._position.x
        diff_y = position.y - cls._position.y
        diff_z = position.z - cls._position.z

        for thing in Creation.things:
            move_x = thing.position.x + diff_x
            move_y = thing.position.y + diff_y
            move_z = thing.position.z + diff_z

            thing.move(Vec3(move_x, move_y, move_z))

    @classmethod
    def load(cls, file_path):
        """ Load a creation from a file """
        Creation.things = pickle.load(open(file_path, "rb"))
        Creation._position = Creation.things[0].position

    @classmethod
    def save(cls, file_path):
        """ Save a creation to a file """
        pickle.dump(Creation.things, open(file_path, "wb"))


