import pygame as pg

import config

class ForcaImage:  
    def __init__(self):
        self.forca_image = pg.image.load("assets/images/forca.png").convert_alpha()
        self.forca_image = pg.transform.scale(self.forca_image, (640, 640))        
  
    def draw(self, surface):
        surface.blit(self.forca_image, (config.WINDOW_WIDTH / 2 - 320, 48))
