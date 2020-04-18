# TODO: at some point this must be a real Singleton
import pickle


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
    def load(cls, file_path):
        """ Load a creation from a file """
        Creation.things = pickle.load(open(file_path, "rb"))

    @classmethod
    def save(cls, file_path):
        """ Save a creation to a file """
        pickle.dump(Creation.things, open(file_path, "wb"))


