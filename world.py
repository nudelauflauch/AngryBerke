import os
import json

class World:
#Pfad übergeben, auf dem liegt die Welt
    def __init__(self, world) -> None:
        self.load_world(world)

    def load_world(self, world) -> None:
        #gibt genauen pfad zu dokumment an
        world_path = f"{os.getcwd()}/gen_world/{world}.json"

        #wenn er das dokumment nicht findet gibt er diese fehlermeldung aus
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
                elif types["type"] == "player_spawn":
                    self.player_spawns = types["positions"]
                    self.player = types["players"]
                elif types["type"] == "opponent_spawns":
                    self.opponent_spawns = types["positions"]