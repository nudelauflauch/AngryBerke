from typing import Optional, Sequence, Tuple
import pymunk
from numpy import rad2deg
<<<<<<< Updated upstream
from pymunk.body import Body
from pymunk.transform import Transform

radius = 50
mass = 10
elasticity = 0.2
friction = 0.4

=======
import pygame.transform

radius = 50
mass = 20
elasticity = 0.2
friction = 0.4
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
=======


class WordRenderObject:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.img = None
    
    def set_img(self, img):
        if not self.img:
            self.img = img.copy()
            self.img = pygame.transform.scale(self.img, (self.width, self.height))
>>>>>>> Stashed changes
