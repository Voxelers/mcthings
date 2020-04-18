from .thing import Thing


# TODO: at some point this must be a real Singleton
class Creation(Thing):
    """
    A creation is a container for all the things built using McThings.
    It can be used to unbuild or build a complete creation. The things
    data will be added during the construction, and it the future it will
    be loaded from a file or other kind of data storage.
    """

    things = []
    """ map with the things in the creation"""

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

