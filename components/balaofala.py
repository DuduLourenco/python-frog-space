import pygame as pg
import cores

class BalaoFala:
    def __init__(self, x, y, text, font, width = 640, height = 464):
        self.text = text
        self.font = font
        
        self.x = x
        self.y = y
        
        self.balao_image = pg.image.load("assets/images/balao.png").convert_alpha()
        self.balao_image = pg.transform.scale(self.balao_image, (width, height))         

    def draw(self, surface, text, text_color = cores.BLACK):
        self.text = text if text != None else self.text
        surface.blit(self.balao_image, (self.x, self.y))
        image_rect = self.balao_image.get_rect(topleft=(self.x, self.y))      
        

        # Renderiza o texto no centro do bolão
        text_surface = self.font.render(self.text, True, text_color)
        text_rect = text_surface.get_rect(center=image_rect.center)
        surface.blit(text_surface, text_rect)