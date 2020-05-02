# TODO: at some point this must be a real Singleton

from mcpi.minecraft import Minecraft
# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

from minecraftstuff import MinecraftDrawing

from .scene import Scene


class Server:
    """
    A Server manages the connection with the Minecraft server.

    Every Scene must have a Server in which built the Scene.
    """

    def __init__(self, host="localhost", port="4711"):
        self._host = host
        self._port = port

        self._mc = Minecraft.create(address=host, port=port)
        self._drawing = MinecraftDrawing(self._mc)

        # To share the connections with all the Things
        Scene.server = self._mc
        Scene.drawing = self._drawing

        self._drawing = None

    @property
    def drawing(self):
        """ Connection to MinecraftDrawing (only used in Things built with MinecraftDrawing)"""
        return self._drawing

    @property
    def mc(self):
        """ Connection to Minecraft """
        return self._mc
