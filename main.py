import pygame as pg
import os
import level_selector
import json


menue_bg = pg.image.load("assets/bg/menue_bg.png")
menue_bg = pg.transform.scale(menue_bg, (1920, 1080))

pg.init()
pg.font.init()
esc_font = pg.font.Font(None, 36)

def gen_level_settings():
    with open("level_progress.save", "w") as progress:
        levels = os.listdir("./gen_world")
        for i, level in enumerate(levels):
            content = level.replace(".json", "") + ":-1"
            if len(levels) - 1 != i:
                content += "\n"

            progress.write(content)

def load_level_progress():
    level_progress = {}
    with open("level_progress.save", "r") as progress:
        for save in progress.readlines():
            content = save.split(":")
            level_progress[content[0]] = int(content[1])

    return level_progress

def init():
    if not os.path.exists("level_progress.save"):
        gen_level_settings()
    else:
        level_progress = load_level_progress()

    levels = []

    for file in os.listdir("./gen_world"):
        with open("./gen_world/" + file, "r") as world:
            world_contend = json.loads(world.read())
            for index in world_contend:
                if index["type"] == "background":
                    levels.append([index["bg"], file.replace(".json", "")])
    
    for i, unpack in enumerate(levels):
        bg, level_name = unpack
        level_bg = pg.image.load("assets/bg/" + bg + ".png")
        try:
            score = level_progress[level_name]
        except KeyError:
            gen_level_settings()
            init()
        levels[i] = level_selector.LevelSelector((i*400 + 50 + i*50, 400), level_bg, score, level_name)

    return levels

def draw(screen, levels):
    screen.fill("white")

    screen.blit(menue_bg, (0,0))

    for i, level in enumerate(levels):
        screen.blit(level.update(), level.pos)

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


def main():
    levels = init()
    
    WINDOW_SIZE = (1920, 1080)
    screen = pg.display.set_mode(WINDOW_SIZE, )#pg.FULLSCREEN)

    FPS = 60
    clock = pg.time.Clock()
    running = True
    is_esc = False
    in_game = False
    tick = 0
    old_esc_tick = 0

    while running:
        tick += 1
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.MOUSEBUTTONDOWN:
                if not is_esc:
                    for level in levels:
                        #starts a new game
                        if (level.pos[0] <= pg.mouse.get_pos()[0] <= level.pos[0] + 400
                            and level.pos[0]<= pg.mouse.get_pos()[1] <= level.pos[1] + 400):
                            world = level.get_level()
                            if world:
                                in_game = True
                                pass
                                #Felix Game connecten
                if is_esc:
                    #handles exit
                    if (960 - 200 <= pg.mouse.get_pos()[0] <= 960 - 200 + 400
                    and 540 - 10 <= pg.mouse.get_pos()[1] <= 540 - 10 + 40):
                        running = False

                    if (960 - 200 <= pg.mouse.get_pos()[0] <= 960 - 200 + 400
                    and 540 - 70 <= pg.mouse.get_pos()[1] <= 540 - 70 + 40):
                        is_esc = False

            if pg.key.get_pressed()[pg.K_ESCAPE]:
                if old_esc_tick + 5 < tick:
                    is_esc = not is_esc
                    old_esc_tick = tick
        
        draw(screen, levels)
        if is_esc:
            draw_esc(screen, in_game)

        pg.display.flip()

if __name__ == "__main__":
    main()