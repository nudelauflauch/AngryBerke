import pygame as pg
import pymunk.pygame_util
import pymunk
import world
import draw
import game_logic


def init(level) -> (tuple[pymunk.Space, world.World, draw.Renderer, game_logic.Game]):

    space = pymunk.Space()
    
    space.gravity = (0, 2000)
    world_obj = world.World(level)
    world_obj.add_to_space(space)

    renderer = draw.Renderer(world_obj)

    game = game_logic.Game(world_obj, space)

    collision_handler = space.add_default_collision_handler()
    collision_handler.post_solve = game.collisions

    return space, world_obj, renderer, game


def mouse_shoot(game:game_logic.Game, world_obj:world.World):

    spawn_area = (
        game.spawn_point[0] - 100,
        game.spawn_point[1] - 100,
        game.spawn_point[0] + 100,
        game.spawn_point[1] + 100,
    )
    
    if (spawn_area[0] - 10 <= pg.mouse.get_pos()[0] <= spawn_area[2] + 10 and spawn_area[1] - 10 <= pg.mouse.get_pos()[1] <= spawn_area[3] + 10):
        if not world_obj.shooting_berke:
            game.spawn_berke(pg.mouse.get_pos())

    elif world_obj.shooting_berke:
        game.shoot_berke(pg.mouse.get_pos())


def handle_main_game(game:game_logic.Game, space:pymunk.Space, world_obj:world.World, screen:pg.Surface, renderer:draw.Renderer, is_esc):
    if not game.win:
        game.tick()
    space.step(1 / 1000)

    if world_obj.shooting_berke:
        game.update_pull(pg.mouse.get_pos())

    screen.fill((255, 255, 255))
    renderer.draw_screen(screen, game.points)

    if game.win:
        world_obj.shooting_berke = None
    else:
        game.check_for_win()

    if is_esc:
        draw.draw_esc(screen, True)
        game.pause()
        # logger_manager.Logger().log("Game", "Pausing game")

    else:
        game.resume()
        # logger_manager.Logger().log("Game", "Resuming game")
