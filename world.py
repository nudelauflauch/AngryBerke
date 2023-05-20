import os

class World
#Pfad übergeben, auf dem liegt die Welt
    def __init__(self, world:os.path) -> None:
        self.load_world(world)

    def load_world(self, world:os.path) -> None:
        world
