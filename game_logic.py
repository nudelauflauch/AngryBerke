import pymunk
import world
import draw
import numpy
import entities
import level_loader

def calculate_distance(point1, point2):
    point1 = numpy.array(point1)
    point2 = numpy.array(point2)
    return numpy.linalg.norm(point2 - point1)

def calculate_angle(point1, point2):
    point1 = numpy.array(point1)
    point2 = numpy.array(point2)
    vector = point2 - point1
    return numpy.arctan2(vector[1], vector[0])

class Game:
    def __init__(self, world: world.World, space: pymunk.Space, logger) -> None:
        self.world = world
        self.space = space
        self.logger = logger

        self.spawn_point = (
            (self.world.player_spawns[2] - self.world.player_spawns[0]) / 2 + self.world.player_spawns[0],
            (self.world.player_spawns[3] - self.world.player_spawns[1]) / 2 + self.world.player_spawns[1],
        )

        self.remove_after_step = []
        self.win = False
        self.points = 0

    def spawn_berke(self, mouse_pos: tuple[int, int]):
        if len(self.world.player) > 0:
            self.logger.log("Shoot", "Spawned new Berke")
            self.world.shooting_berke = draw.PulledBerke(mouse_pos, self.spawn_point)
        else:
            self.logger.log("Shoot", "Out of Berkes")


    def shoot_berke(self, mouse_pos):
        self.logger.log("Shoot", "Shooting Berke")

        body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        body.position = mouse_pos

        self.berke_entity = entities.Berke(body)

        self.world.entities.append(self.berke_entity)
        
        line = pymunk.Segment(body, (0,0), (0,0), 5)
        line.mass = 8

        self.world.entities.append(self.berke_entity)

        self.space.add(self.berke_entity, body, line)

        angle = calculate_angle(mouse_pos, self.spawn_point)
        distance = calculate_distance(mouse_pos, self.spawn_point)

        fx = numpy.cos(angle) * distance * 200
        fy = numpy.sin(angle) * distance * 200

        self.berke_entity.body.apply_impulse_at_local_point((fx, fy), (0,0))

        self.world.shooting_berke = None

        self.world.player.pop(0)


    def update_pull(self, mouse_pos: tuple[int, int]):
        self.world.shooting_berke.update_pos(mouse_pos)


    def start(self):
        self.logger.log("GameStart", "Making moveable")

        self.change_moveability(pymunk.Body.DYNAMIC)


    def change_moveability(self, move_type):
        for wood in self.world.world_bodies:
            wood.body.body_type = move_type

        for entity in self.world.entities:
            entity.body.body_type = move_type

        return self.space

    def tick(self):
        self.safe_remove()

        if self.win:
            self.logger.log("GameStop", "Making not moveable")
            self.change_moveability(pymunk.Body.STATIC)

    def safe_remove(self):
        for shapes in self.remove_after_step: 
            for shape in shapes:
                try:
                    self.space.remove(shape)
                except:
                    pass

    @staticmethod
    def check_instance(test_obj, class1, class2) -> bool:
        return (isinstance(test_obj[0], class1) and isinstance(test_obj[1], class2)) or (isinstance(test_obj[1], class1) and isinstance(test_obj[0], class2))

    def collisions(self, arbiter:pymunk.Arbiter, space:pymunk.Space, data):
        shapes = arbiter.shapes
        impuls = numpy.linalg.norm(arbiter.total_impulse[0] - arbiter.total_impulse[1])

        def remove_pig(shapes):
            destroy = False
            if isinstance(shapes[0], entities.Pig) and not isinstance(shapes[0], entities.Berke):
                destroy = True
                try:
                    self.world.entities.remove(shapes[0])
                    self.logger.log("Destroy", "Destroying Pig")
                except ValueError:
                    pass
                self.remove_after_step.append([shapes[0], shapes[0].body])

            elif isinstance(shapes[1], entities.Pig) and not isinstance(shapes[1], entities.Berke):
                destroy = True
                try:
                    self.world.entities.remove(shapes[1])
                    self.logger.log("Destroy", "Destroying Pig")
                except ValueError:
                    pass
                self.remove_after_step.append([shapes[1], shapes[1].body])
            
            if destroy:
                self.points += 1000 + impuls/4
                

        def remove_wood(shapes):
            destroy = False
            if not isinstance(shapes[0], entities.Pig) and shapes[0].body.body_type != pymunk.Body.STATIC:
                self.remove_after_step.append([shapes[0], shapes[0].body])
                destroy = True
                try:
                    self.world.world_bodies.remove(shapes[0])
                    self.logger.log("Destroy", "Destroying Wood")
                except ValueError:
                    pass

            elif not isinstance(shapes[1], entities.Pig) and shapes[1].body.body_type != pymunk.Body.STATIC:
                self.remove_after_step.append([shapes[1], shapes[1].body])
                destroy = True
                try:
                    self.world.world_bodies.remove(shapes[1])
                    self.logger.log("Destroy", "Destroying Wood")
                except ValueError:
                    pass
            
            if destroy:
                self.points += 1000 + impuls/4


        #if pig and a berke is touching direktly
        if Game.check_instance(shapes, entities.Pig, entities.Berke):
            if impuls > 2500:
                remove_pig(shapes)
    

        #checks if a pig is touched by a wood
        elif isinstance(shapes[0], entities.Pig) or isinstance(shapes[1], entities.Pig):
            if impuls > 5000:
                remove_pig(shapes)
        

        #ehckes if a wood should be deleted
        elif not isinstance(shapes[0], entities.Pig) or not isinstance(shapes[1], entities.Pig):
            if impuls > 6000:
                remove_wood(shapes)     

        return True
    
    def check_for_win(self):
        win = True
        for pig in self.world.entities:
            if isinstance(pig, entities.Pig) and not isinstance(pig, entities.Berke):
                win = False
        
        if win:
            self.win = True
            level_loader.save_progress(3, self.world.world_name)
            self.logger.log("GameStop", "Game is over: Win")
        
        if len(self.world.player) == 0 and not self.win:
            self.logger.log("GameStop", "Game is over: Lose")