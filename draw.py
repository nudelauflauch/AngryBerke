import pygame as pg
import os
import world
import numpy
import entities


pg.font.init()
stat_font = pg.font.Font(None, 50)
esc_font = pg.font.Font(None, 36)

# Hintergrund Grau/ Grüne Buttons/ schwarz (0,0,0)   
def draw_esc(screen, in_game):
    gray = pg.Surface((1920, 1080))
    gray.fill((211, 211, 211))
    gray.set_alpha(150)
    screen.blit(gray, (0,0))

    pg.draw.rect(screen, (42, 173, 21), (960 - 200, 540 - 20, 400, 40))
    pg.draw.rect(screen, (42, 173, 21), (960 - 200, 540 - 80, 400, 40))

    screen.blit(esc_font.render("Resume", True, (0,0,0)), (960 - 200, 540 - 70))
    screen.blit(esc_font.render("Exit To Desktop", True, (0,0,0)), (960 - 200, 540 - 10))

    if in_game:
        pg.draw.rect(screen, (42, 173, 21), (960 - 200, 540 + 40, 400, 40))
        screen.blit(esc_font.render("Return To Menue", True, (0,0,0)), (960 - 200, 540 + 50))

        

class PulledBerke:
    rope_img = pg.image.load(os.getcwd() + "/assets/rope.png")

    def __init__(self, pos, pull_point) -> None:
        self.pos = pos
        self.pull_point = pull_point

    def update_pos(self, pos):
        self.pos = pos

    def update_screen(self, screen:pg.Surface) -> pg.Surface:
        self.rope_len = numpy.sqrt(numpy.power(self.pos[0] - self.pull_point[0], 2) + numpy.power(self.pos[1] - self.pull_point[1], 2))
        rope_img = pg.transform.scale(self.rope_img, (self.rope_len, 20))

        self.angle = numpy.rad2deg(numpy.arcsin((self.pos[1] - self.pull_point[1]) / self.rope_len))

        rope_img = pg.transform.rotate(rope_img, self.angle)

        if self.pos[0] < self.pull_point[0]:
            if self.pos[1] > self.pull_point[1]:
                #down left
                screen.blit(rope_img, (self.pos[0], self.pos[1] -  rope_img.get_height() + 20))
            else:
                #up left
                screen.blit(rope_img, self.pos)
        elif self.pos[0] > self.pull_point[0]:
            if self.pos[1] > self.pull_point[1]:
                #down right
                screen.blit(pg.transform.flip(rope_img, True, False), (self.pos[0] - rope_img.get_width() + 20, self.pos[1]  - rope_img.get_height() + 20))
            else:
                #up right
                screen.blit(pg.transform.flip(rope_img, True, False), (self.pos[0] - rope_img.get_width() + 20, self.pos[1]))

        pg.draw.circle(screen, (255, 255, 255), self.pull_point, 30)
        screen.blit(pg.transform.scale(Renderer.berke_img, (entities.radius, entities.radius)), (self.pos[0] - entities.radius/2, self.pos[1] - entities.radius/2))
    

    def flip_rope(self, rope_len, rope_img, screen) -> pg.Surface:
        angle = numpy.rad2deg(numpy.arcsin((self.pos[1] - self.pull_point[1]) / rope_len))

        rope_img = pg.transform.rotate(rope_img, angle)

        if self.pos[0] < self.pull_point[0] and self.pos[1] > self.pull_point[1]:
            return screen.blit(rope_img, (self.pos[0] + rope_img.get_height(), self.pos[1]))
        elif self.pos[0] > self.pull_point[0]:
            if self.pos[1] > self.pull_point[1]:
                return pg.transform.flip(rope_img, False, True)
            return pg.transform.flip(rope_img, True, True)
        return rope_img
        


class Renderer:
    pig_img = pg.image.load(os.getcwd() + "/assets/pig.png")
    berke_img = pg.image.load(os.getcwd() + "/assets/berke.png")
    wood_img = pg.image.load(os.getcwd() + "/assets/wood.png")
    stone_img = pg.image.load(os.getcwd() + "/assets/stone.png")
    slingshot_img = pg.image.load(os.getcwd() + "/assets/slingshot.png")

    bg_img = pg.image.load(os.getcwd() + "/assets/bg/2.png")

    def __init__(self, world_obj: world.World) -> None:

        self.world = world_obj

        # resizes the slingshot
        self.slingshot_img = self.resize(self.slingshot_img, self.world.player_spawns)

        Renderer.bg_img = pg.transform.scale(Renderer.bg_img, (1920, 1080))
        Renderer.berke_img = pg.transform.scale(Renderer.berke_img, (entities.radius*2, entities.radius*2))
        Renderer.pig_img = pg.transform.scale(Renderer.pig_img, (entities.radius*2, entities.radius*2))

    def draw_screen(self, screen: pg.Surface, points):
        screen.blit(Renderer.bg_img, (0,0))

        #draws the stone (solid blocks) on screen
        for stone in self.world.sollid_bodies:
            stone_img = self.resize(self.stone_img, stone.bb)
            pos = self.get_pos_of_sollid(stone.bb)
            screen.blit(stone_img, pos)

        # draws all wood_blocks on screen
        for wood in self.world.world_bodies:

            shape_width = wood.bb.right - wood.bb.left
            shape_height = wood.bb.top - wood.bb.bottom
            angle = numpy.rad2deg(wood.body.angle)

            scaled_image = pg.transform.scale(Renderer.wood_img, (int(shape_width), int(shape_height)))
            rotated_image = pg.transform.rotate(scaled_image, -angle)

            pos = self.get_pos_of_sollid(wood.bb)
            screen.blit(rotated_image,  (wood.bb.left, wood.bb.bottom))

        # draws the slingshot on screen
        screen.blit(Renderer.slingshot_img, self.world.player_spawns)

        # draws all entites on the screen
        for entity in self.world.entities:
            if isinstance(entity, entities.Berke):
                berke_img = pg.transform.rotate(Renderer.berke_img, entity.get_rot())
                berke_img = self.resize(berke_img, entity.bb)
                pos = entity.body.position
                screen.blit(berke_img, [pos[0] - entity.radius, pos[1] - entity.radius])

            else:
                rot = entity.get_rot()
                pig_img = pg.transform.rotate(Renderer.pig_img, rot)
                pig_img = self.resize(pig_img, entity.bb)
                pos = entity.body.position
                screen.blit(pig_img, [pos[0] - entity.radius, pos[1] - entity.radius])

        if self.world.shooting_berke:
            self.world.shooting_berke.update_screen(screen)

        screen.blit(stat_font.render(str(int(round(points, 0))), True, "white"), (1700, 40))

    @staticmethod
    def get_pos_of_sollid(bounder_box):
        return bounder_box[0], bounder_box[1]

    @staticmethod
    def resize(img, bounderies) -> pg.Surface:
        x_len = bounderies[2] - bounderies[0]
        y_len = bounderies[3] - bounderies[1]

        return pg.transform.scale(img.copy(), (x_len, y_len))