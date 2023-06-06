import pymunk

class Pig(pymunk.Circle):
    p_radius = 50
    mass = 500
    elasticity = 0.9
    friction = 0.4

    def __init__(self, body) -> None:
        super().__init__(body, Pig.p_radius)
        self.angle = 0

    def update_rot(self):
        self.angle = self.body.angle


class Berke(Pig):
    pass
