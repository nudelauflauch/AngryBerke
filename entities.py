from typing import Optional, Sequence, Tuple
import pymunk
from numpy import rad2deg
from pymunk.body import Body
from pymunk.transform import Transform

radius = 50
mass = 10
elasticity = 0.2
friction = 0.4


class Pig(pymunk.Circle):
    
    def __init__(self, body:pymunk.Shape) -> None:
        super().__init__(body, radius)
        self.mass = mass
        self.elasticity = elasticity
        self.friction = friction

    def get_rot(self):
        return -rad2deg(self.body.angle)


class Berke(Pig):
    def __init__(self, body: pymunk.Shape) -> None:
        super().__init__(body)
