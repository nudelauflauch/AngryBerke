import pygame, os, numpy

<<<<<<< Updated upstream
class LevelSelector:
    # Konstruktor von level-selector 
    def __init__(self, pos, img, score, level_name) -> None:
        self.pos = pos
    # Skaliert das Bild auf eine Größe von 360x300 Pixeln
        self.img = pygame.transform.scale(img, (360, 300))
        self.score = score
        self.level_name = level_name

    # Macht die Level, die noch nicht auswählbar sind grau 
        if score == -1:
=======
#class for the main game to draw each level
class LevelSelector:
    def __init__(self, pos, img, score, level_name) -> None:
        self.pos = pos
        self.img = pygame.transform.scale(img.copy(), (360, 300))
        self.score = score
        self.level_name = level_name
        self.star_img = pygame.transform.scale(pygame.image.load(os.getcwd() + "/assets/star.png"), (60,60))

        if score == -1:
            #converts the image to a gray scaled image
>>>>>>> Stashed changes
            arr = pygame.surfarray.array3d(self.img)
            avgs = [[(r*0.298 + g*0.587 + b*0.114) for (r,g,b) in col] for col in arr]
            arr = numpy.array([[[avg,avg,avg] for avg in col] for col in avgs])
            self.img = pygame.surfarray.make_surface(arr)

<<<<<<< Updated upstream
    # Wenn der Fortschritt größer als 3 ist / Maximalwert für die Punktzahl
        elif score > 3:
            self.score = 3

    # Laden & Skalieren auf 60x60 Pixel
        self.star_img = pygame.transform.scale(pygame.image.load(os.getcwd() + "/assets/star.png"), (60,60))

    # Entstehung Level-Icons 
    def update(self):

=======
        elif score > 3:
            self.score = 3

    #gets called to get a new Surface for the screen
    def update(self):
>>>>>>> Stashed changes
        surface = pygame.Surface((400,400))

        surface.fill((195, 195, 195))

        surface.blit(self.img, (20, 20))

        for i in range(self.score):
            surface.blit(self.star_img, (i*120 + 40, 330))

<<<<<<< Updated upstream
    # Zurückgeben der Oberfläche 
        return surface
    
    def get_level(self):
    # Überprüft, ob das Level gespielt wurde
        if self.score != -1:
    #Zurückgebne Level-Name 
            return self.level_name
    #Rückgabe wenn Level nicht gespielt wurde 
=======
        return surface
    
    def get_level(self):
        if self.score != -1:
            return self.level_name
>>>>>>> Stashed changes
        return None
