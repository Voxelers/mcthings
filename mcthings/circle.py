from mcthings.scene import Scene
from mcthings.thing import Thing


class Circle(Thing):

    radius = None
    """ radius of the Sphere """

    def build(self):
        Scene.drawing.drawCircle(
            self.position.x,
            self.position.y,
            self.position.z,
            self.radius,
            self.block)
        self._end_position = self.position
