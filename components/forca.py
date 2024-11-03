import pygame as pg

import config

class ForcaImage:  
    def __init__(self):
        self.forca_image = pg.image.load("assets/images/forca.png").convert_alpha()
        self.forca_image = pg.transform.scale(self.forca_image, (640, 640))   
        
        self.forca_sapo_images = [
            pg.image.load("assets/images/sapo_forca_0.png").convert_alpha(),
            pg.image.load("assets/images/sapo_forca_1.png").convert_alpha(),
            pg.image.load("assets/images/sapo_forca_2.png").convert_alpha(),
            pg.image.load("assets/images/sapo_forca_3.png").convert_alpha(),
            pg.image.load("assets/images/sapo_forca_4.png").convert_alpha(),
            pg.image.load("assets/images/sapo_forca_5.png").convert_alpha(),
            pg.image.load("assets/images/sapo_forca_6.png").convert_alpha()
        ]        
  
    def draw(self, surface, erros = 0):
        surface.blit(self.forca_image, (config.WINDOW_WIDTH / 2 - 320, 48))
        
        if(erros > len(self.forca_sapo_images) - 1):
            erros = len(self.forca_sapo_images) - 1
        self.forca_sapo_image = pg.transform.scale(self.forca_sapo_images[erros], (300, 300))
        surface.blit(self.forca_sapo_image, (config.WINDOW_WIDTH / 2 - 162, 160))