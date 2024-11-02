import pygame as pg

import config
import cores

from components.advicetext import AdviceText
from components.button import Button

class Game:
  def __init__(self):
    pg.init()
    self.clock = pg.time.Clock()
    pg.display.set_caption(config.TITLE)
    self.surface = pg.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    self.loop = True
    
    # carrega a imagem de fundo
    self.background_image = pg.image.load("assets/images/menu.jpg").convert()
    self.background_image = pg.transform.scale(self.background_image, (config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    
    pg.font.init()
    
    self.fonts = {
      'smalltest': pg.font.SysFont('Inter', 16),
      'small': pg.font.SysFont('Inter', 24)
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
    
    self.advice_text = AdviceText(
      font=self.fonts["small"],
    )
    
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
    
    self.menu()
    
    pg.display.flip()
    self.clock.tick(config.FPS)
    
  def menu(self):
    self.surface.blit(self.background_image, (0, 0))
    
    version_text = self.fonts["small"].render(config.VERSION, True, cores.BLACK)
    version_text_rect = version_text.get_rect(bottomright=(config.WINDOW_WIDTH - 16, config.WINDOW_HEIGHT - 16))
    self.surface.blit(version_text, version_text_rect)
    
    # sapos_nao_maltratados_text = self.fonts["smalltest"].render("*Quase nenhum sapo foi afetado durante o desenvolvimento desse jogo*", True, cores.BLACK)
    # sapos_nao_maltratados_text_rect = sapos_nao_maltratados_text.get_rect(bottomleft=(12, config.WINDOW_HEIGHT - 12))
    # self.surface.blit(sapos_nao_maltratados_text, sapos_nao_maltratados_text_rect)
    
    self.advice_text.draw(self.surface)
    
        
    self.start_button.check_hover(self.mouse_pos)
    self.start_button.draw(self.surface)    
    if(self.start_button.is_clicked(self.mouse_pos, self.mouse_pressed)):
      print("Começar!!!")

def main():
  game = Game()
  game.main()
  
main()