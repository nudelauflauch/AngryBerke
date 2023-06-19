import pygame as pg
import main_game
import draw
import level_loader
import logger_manager
import traceback

<<<<<<< Updated upstream
# Laden des Hintergrundbildes für das Menü
menue_bg = pg.image.load("assets/bg/menue_bg.png")
menue_bg = pg.transform.scale(menue_bg, (1920, 1080))

# Initialisierung des Loggers
=======
menue_bg = pg.image.load("assets/bg/menue_bg.png")
menue_bg = pg.transform.scale(menue_bg, (1920, 1080))
>>>>>>> Stashed changes
logger = logger_manager.Logger()

def draw_menu(screen:pg.Surface, levels):
    screen.fill("white")

    screen.blit(menue_bg, (0,0))

<<<<<<< Updated upstream
    for i, level in enumerate(levels):
        screen.blit(level.update(), level.pos)

# Hauptfunktion
def main():
# Initialisierung von Pygame
    pg.init()

    levels = level_loader.init_levels()
    logger.log("Starting", "Found levels: ", len(levels))
=======
    for level in levels:
        screen.blit(level.update(), level.pos)


def main():
    pg.init()

    levels = level_loader.init_levels()
    logger_manager.log("Starting", "Found levels: ", len(levels))
>>>>>>> Stashed changes
    
    WINDOW_SIZE = (1920, 1080)
    screen = pg.display.set_mode(WINDOW_SIZE, )# pg.FULLSCREEN)

    FPS = 1000
    clock = pg.time.Clock()
<<<<<<< Updated upstream
=======
    game = None
>>>>>>> Stashed changes
    running = True
    is_esc = False
    in_game = False
    tick = 0
    old_esc_tick = 0

<<<<<<< Updated upstream
    logger.log("Starting", "Init complet, starting game loop")

#Main-Loop
=======
    logger_manager.log("Starting", "Init complet, starting game loop")

>>>>>>> Stashed changes
    while running:
        tick += 1
        clock.tick(FPS)
        if in_game:
            space.step(1/1000)    

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.MOUSEBUTTONDOWN:
<<<<<<< Updated upstream
=======
                if in_game and game.win:
                    in_game = False
                    is_esc = False
                    levels = level_loader.init_levels()
                    logger_manager.log("GameStop", "Exiting to menue")

>>>>>>> Stashed changes
                if not is_esc and not in_game:
                    for level in levels:
                        #tries to starts a new game
                        if level.pos[0] <= pg.mouse.get_pos()[0] <= level.pos[0] + 400 and level.pos[1]<= pg.mouse.get_pos()[1] <= level.pos[1] + 400:
                            world = level.get_level()
        
                            if world:
<<<<<<< Updated upstream
                                space, world_obj, renderer, game = main_game.init(world, logger)
                                game.start()
                                in_game = True
                                logger.log("GameStart", "Starting game", world)
                
                if in_game:
                    main_game.mouse_shoot(game, world_obj, logger)
=======
                                space, world_obj, renderer, game = main_game.init(world)
                                game.start()
                                in_game = True
                                logger_manager.log("GameStart", "Starting game", world)
                
                if in_game:
                    main_game.mouse_shoot(game, world_obj)
>>>>>>> Stashed changes
                        
                
                #handles escape mouse presses         
                if is_esc:
                    if (960 - 200 <= pg.mouse.get_pos()[0] <= 960 - 200 + 400
                    and 540 - 10 <= pg.mouse.get_pos()[1] <= 540 - 10 + 40):
                        running = False

                    if (960 - 200 <= pg.mouse.get_pos()[0] <= 960 - 200 + 400
                    and 540 - 70 <= pg.mouse.get_pos()[1] <= 540 - 70 + 40):
                        is_esc = False
                    
                    if in_game:
                        if (960 - 200 <= pg.mouse.get_pos()[0] <= 960 - 200 + 400
                        and 540 + 40 <= pg.mouse.get_pos()[1] <= 540 + 40 + 40):
                            in_game = False
                            is_esc = False
                            levels = level_loader.init_levels()
<<<<<<< Updated upstream
                            logger.log("GameStop", "Exiting to menue")

            if pg.key.get_pressed()[pg.K_ESCAPE]:
                if old_esc_tick + 30 < tick:
                    is_esc = not is_esc
                    old_esc_tick = tick
=======
                            logger_manager.log("GameStop", "Exiting to menue")

            if pg.key.get_pressed()[pg.K_ESCAPE]:
                if not game:
                    win = False
                else:
                    win = game.win
                if old_esc_tick + 50 < tick and not(in_game and win):
                    is_esc = not is_esc
                    old_esc_tick = tick
                    if game:
                        game.old_ecs_tick = game.ticks
>>>>>>> Stashed changes

        
        if tick%16 == 0:
            if in_game:
                main_game.handle_main_game(game, space, world_obj, screen, renderer, is_esc)
<<<<<<< Updated upstream
# Außerhalb des Speils / im Menue
=======

                if game.win:
                    renderer.draw_win(screen, game.points)

>>>>>>> Stashed changes
            else:
                draw_menu(screen, levels)
                if is_esc:
                    draw.draw_esc(screen, False)

        pg.display.flip()
<<<<<<< Updated upstream
        
# Startet das spiel
=======

>>>>>>> Stashed changes
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
<<<<<<< Updated upstream
        logger.log("ERROR", "KeyboardInterrupt")
    except BaseException as e:
        print(e)
        logger.log("ERROR", traceback.format_exc())
    logger.stop_logging()
=======
        logger_manager.log("ERROR", "KeyboardInterrupt: Stopped thee game because of a keyboard interrupt")
    except BaseException as e:
        logger_manager.log("ERROR", traceback.format_exc())
    logger_manager.stop_logging()
>>>>>>> Stashed changes
