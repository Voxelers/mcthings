# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import mcpi.block
import mcpi.vec3

from ._version import __version__
from .scene import Scene

from .utils import build_schematic_nbt
from .world import World


class Thing:
    """ base class for all objects in mcthings library """

    block = mcpi.block.BRICK_BLOCK
    """ block type used by the thing. Default to BRICK_BLOCK """
    _block_empty = mcpi.block.AIR
    """ block type used to remove blocks in this Thing """

    def __init__(self, position, parent=None, scene=None):
        """
        Create a thing
        :param position: build position
        :param parent: parent Thing in which this one is included
        :param scene: scene in which this Thing is included
        """

        self._end_position = None
        self._parent = parent
        self._children = []
        self._position = None
        self._decorators = []
        self._scene = scene

        if position:
            self._position = mcpi.vec3.Vec3(position.x, position.y, position.z)

        if scene is None:
            # If no Scenes exists yet, create a new one
            if not World.scenes:
                Scene()  # Scene add itself to the World

            """ Use the default  Scene """
            self._scene = World.first_scene()

        # Add then thing built to the scene
        if parent is None:
            self._scene.add(self)

        # McThing version which created this Thing
        self._version = __version__

    @property
    def end_position(self):
        """ end position of the thing """
        return self._end_position

    @property
    def position(self):
        """ initial position of the thing """
        return self._position

    @property
    def parent(self):
        """ parent Thing in which this one is included """
        return self._position

    @property
    def scene(self):
        """ scene which this thing is included """
        return self._scene

    def add_child(self, child):
        """ Add a children to this Thing  """
        self._children.append(child)

    def build(self):
        """
        Build the thing and show it in Minecraft at position coordinates

        :return:
        """

    def unbuild(self):
        """
        Unbuild the thing in Minecraft

        :return:
        """

        block = self.block
        self.block = self._block_empty
        self.build()
        self.block = block

    def move(self, position):
        """
        Move the thing to a new position

        :param position: new position
        :return:
        """

        self.unbuild()
        self._position = position
        self.build()

    def to_schematic(self, file_path, blocks_data=False):
        """
        Convert the Thing to a Schematic Object

        :file_path: file in which to export the Thing in Schematic format
        :blocks_data: include blocks data (much slower)
        :return: the Schematic object
        """

        build_schematic_nbt(self.position, self.end_position, blocks_data).write_file(file_path)

    def add_decorator(self, decorator):
        """
        Add a new Decorator to be called once the Thing is decorated

        :param decorator: a Decorator to be called
        :return:
        """
        self._decorators.append(decorator)

    def decorate(self):
        """
        Call all decorators for the current Thing

        :return:
        """
        for decorator in self._decorators:
            decorator.decorate(self)
            for child in self._children:
                decorator.decorate(child)

    def find_bounding_box(self):
        """ Compute the bounding box of the Thing """

        return self.position, self.end_position
