import os
import json
import pymunk
import pygame
import pymunk.pygame_util
import entities


class World:
    def __init__(self, world):
        self.load_world(world)

        self.shooting_berke = None

    def load_world(self, world):
        world_path = f"{os.getcwd()}/gen_world/{world}.json"

        if not os.path.exists(world_path):
            raise FileNotFoundError(f"Path {world_path} is not existing.")

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
                    self.player = types["players"]
                elif types["type"] == "opponent_spawns":
                    self.opponent_spawns = types["positions"]

    def add_to_space(self, space):
        self.space = space
        self.world_bodys = []
        self.entities = []

        for wood, sollid, player, opponent in zip(
            self.wood_blocks,
            self.sollid_blocks,
            self.player_spawns,
            self.opponent_spawns,
        ):
            self.wood_blocks.append(self.add_static(wood))

            self.add_static(sollid)
            opponent = self.add_pigs_berke(opponent)

            self.entities.append(opponent)

    def add_static(self, coordinates):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = coordinates[0:2]

        shape = pymunk.Poly.create_box(body, coordinates[2:4])
        shape.mass = 10
        shape.elasticity = 0.9
        shape.friction = 0.4
        shape.color = (255, 0, 0, 255)
        self.space.add(body, shape)

        return shape

    def add_pigs_berke(self, coordinates, is_pig=True):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = coordinates[0:2]

        if is_pig:
            shape = entities.Pig(body)
        else:
            shape = entities.Berke(body)
        self.space.add(body, shape)

        return shape
