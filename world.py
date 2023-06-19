import os
import json
import pymunk
import pymunk.pygame_util
import entities


class World:
    def __init__(self, world: os.path):
        self.load_world(world)

        self.world_name = world
        self.shooting_berke = None

<<<<<<< Updated upstream
=======
    #loads the world from the json data
>>>>>>> Stashed changes
    def load_world(self, world: os.path):
        world_path = f"{os.getcwd()}/gen_world/{world}.json"

        if not os.path.exists(world_path):
            raise FileNotFoundError(f"Path {world_path} does not existing.")

        with open(world_path, "r") as world_file:
            world_contend = world_file.read()
            world_contend = json.loads(world_contend)

            for types in world_contend:
                if types["type"] == "wood_blocks":
                    self.wood_blocks = types["positions"]

                elif types["type"] == "sollid_blocks":
                    self.sollid_blocks = types["positions"]

                elif types["type"] == "player_spawns":
                    self.player_spawns = types["positions"]
<<<<<<< Updated upstream
                    self.player = types["players"]
=======
                    self.players = types["players"]
>>>>>>> Stashed changes

                elif types["type"] == "opponent_spawns":
                    self.opponent_spawns = types["positions"]

    #addes every entity to the space
    def add_to_space(self, space):
        self.space = space

        self.world_bodies = []
        self.sollid_bodies = []
        self.entities = []

        for wood in self.wood_blocks:
            self.world_bodies.append(self.add_static(wood))

        for sollid in self.sollid_blocks:
            self.sollid_bodies.append(self.add_static(sollid))
            
        for opponent in self.opponent_spawns:
            opponent = self.add_pigs_berke(opponent)
            self.entities.append(opponent)
    

<<<<<<< Updated upstream
        return self.space
    

=======
    #addes a new static object to the space
>>>>>>> Stashed changes
    def add_static(self, coordinates):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = coordinates[0:2]

        if len(coordinates) == 5:
            body.angle = coordinates[4]

        shape = pymunk.Poly.create_box(body, coordinates[2:4])
        shape.mass = 10
        shape.elasticity = 0.3
        shape.friction = 1

        self.space.add(body, shape)

        word_renderer_obj = entities.WordRenderObject(*coordinates[2:4])

        return (shape, word_renderer_obj)


    #adds a entity to the world
    def add_pigs_berke(self, coordinates, is_pig=True):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = coordinates[0:2]

        if is_pig:
            shape = entities.Pig(body)
        else:
            shape = entities.Berke(body)
        self.space.add(body, shape)

        return shape
