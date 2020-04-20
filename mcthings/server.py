# TODO: at some point this must be a real Singleton

from mcpi.minecraft import Minecraft
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
        Scene.server = self._mc

        self._drawing = None

    @property
    def drawing(self):
        """ Connection to MinecraftDrawing (only used in Things built with MinecraftDrawing)"""

        if self._drawing is None:
            from minecraftstuff import MinecraftDrawing
            self._drawing = MinecraftDrawing(self._mc)

        return self._drawing

    @property
    def mc(self):
        """ Connection to Minecraft """
        return self._mc
