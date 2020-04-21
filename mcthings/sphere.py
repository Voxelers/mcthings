from mcthings.scene import Scene
from mcthings.thing import Thing


class Sphere(Thing):

    radius = None
    """ radius of the Sphere """

    def build(self):
        Scene.drawing.drawSphere(
            self.position.x,
            self.position.y,
            self.position.z,
            self.radius,
            self.block)
        self._end_position = self.position


class SphereHollow(Thing):

    radius = None
    """ radius of the Hollow Sphere """

    def build(self):
        Scene.drawing.drawHollowSphere(
            self.position.x,
            self.position.y,
            self.position.z,
            self.radius,
            self.block)
        self._end_position = self.position

