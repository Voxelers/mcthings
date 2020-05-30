from mcpi.minecraft import Minecraft
# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

from minecraftstuff import MinecraftDrawing


class Server:
    """
    A Server manages the connection with the Minecraft server.

    Every World must have a Server in which built the World.
    """

    def __init__(self, host="localhost", port="4711"):
        self._host = host
        self._port = port

        self._mc = Minecraft.create(address=host, port=port)
        self._drawing = MinecraftDrawing(self._mc)

    @property
    def drawing(self):
        """ Connection to MinecraftDrawing (only used in Things built with MinecraftDrawing)"""
        return self._drawing

    @property
    def mc(self):
        """ Connection to Minecraft """
        return self._mc
