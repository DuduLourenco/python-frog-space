import pygame as pg

import os

import config
import cores

from components.advicetext import AdviceText
from components.versiontext import VersionText
from components.button import Button
from components.background import BackgroundImage

os.environ['SDL_VIDEO_WINDOW_POS'] = "16,48"

class Game:
  def __init__(self):
    pg.init()
    self.clock = pg.time.Clock()
    pg.display.set_caption(config.TITLE)
    self.surface = pg.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    self.loop = True
    
    self.scene = "menu"
    
    pg.font.init()
    
    self.fonts = {
      'smalltest': pg.font.SysFont('Inter', 20),
      'small': pg.font.SysFont('Inter', 24),
      'medium': pg.font.SysFont('Inter', 32),
      'large': pg.font.SysFont('Inter', 40),
      'title': pg.font.SysFont('Inter', 64)
    }
    
    self.start_button = Button(
      x=config.WINDOW_WIDTH // 2 - 100, 
      y=config.WINDOW_HEIGHT // 2 - 25, 
      width=200, 
      height=50, 
      text="Começar", 
      font=self.fonts["small"], 
      color_normal=cores.GRAY, 
      color_hover=cores.LIGHT_GRAY
    )
    
    self.menu_button = Button(
      x=config.WINDOW_WIDTH - 100 - 16, 
      y=16, 
      width=100, 
      height=25, 
      text="Menu", 
      font=self.fonts["small"], 
      color_normal=cores.GRAY, 
      color_hover=cores.LIGHT_GRAY
    )
    
    self.advice_text = AdviceText(
      font=self.fonts["smalltest"],
    )
    
    self.version_text = VersionText(
      font=self.fonts["smalltest"],
    )
    
    self.background_image = BackgroundImage()    
    self.sapo_advogado_image = pg.image.load("assets/images/sapo_advogado.png").convert_alpha()      
    self.sapo_advogado_image = pg.transform.scale(self.sapo_advogado_image, (150, 466))
    
  def main(self):
    while self.loop:
      self.game_loop()
    pg.quit()
    
  def game_loop(self):
    self.mouse_pos = pg.mouse.get_pos()
    self.mouse_pressed = pg.mouse.get_pressed()
    
    for event in pg.event.get():
      if event.type == pg.QUIT:
        self.loop = False
        
    self.surface.fill(cores.WHITE)
    self.background_image.draw(self.surface)
    
    if self.scene == "menu":
      self.menu()
    elif self.scene == "game":
      self.game()
    else:
      self.menu()
      
    self.version_text.draw(self.surface) 
    self.advice_text.draw(self.surface) 
    
    pg.display.flip()
    self.clock.tick(config.FPS)
    
  def menu(self):        
    title_text = self.fonts["title"].render("A FORCA", True, cores.BLACK)
    title_text_rect = title_text.get_rect(center=(config.WINDOW_WIDTH / 2, config.WINDOW_HEIGHT / 4))
    self.surface.blit(title_text, title_text_rect)      
        
    self.start_button.check_hover(self.mouse_pos)
    self.start_button.draw(self.surface)    
    if(self.start_button.is_clicked(self.mouse_pos, self.mouse_pressed)):
      self.scene = "game"
      
  def game(self):    
    self.surface.blit(self.sapo_advogado_image, (config.WINDOW_WIDTH - 150, config.WINDOW_HEIGHT - 466))
    
    you_text = self.fonts["small"].render("Sapu (Você)", True, cores.WHITE)
    you_text_rect = you_text.get_rect(bottomright=(config.WINDOW_WIDTH - 40, config.WINDOW_HEIGHT - 466 - 16))
    self.surface.blit(you_text, you_text_rect) 
    
    self.menu_button.check_hover(self.mouse_pos)
    self.menu_button.draw(self.surface)    
    if(self.menu_button.is_clicked(self.mouse_pos, self.mouse_pressed)):
      self.scene = "menu"

def main():
  game = Game()
  game.main()
  
main()