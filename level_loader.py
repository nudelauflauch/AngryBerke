import os, json, level_selector, pygame

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

def init_levels():
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
    
    return_levels = [" " for i in range(len(levels))]

    for i, unpack in enumerate(levels):
        bg, level_name = unpack
        level_bg = pygame.image.load("assets/bg/" + bg + ".png")
        try:
            score = level_progress[level_name]
        except KeyError:
            gen_level_settings()
            init_levels()

        if i == 0 and score == -1:
            score = 0
        elif level_progress[levels[i-1][1]] > 0 and score == -1:
            score = 0
        
        return_levels[i] = level_selector.LevelSelector((i*400 + 50 + i*50, 400), level_bg, score, level_name)

    return return_levels

def save_progress(stars, level):
    content = ""
    with open("level_progress.save", "r") as progress:
        for save in progress.readlines():
            if save.split(":")[0] == level:
                content += f"{level}:{stars}\n"
            else:
                content += save

    with open("level_progress.save", "w") as progress:
        progress.write(content)