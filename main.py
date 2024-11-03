import pygame as pg
import random

import time

import os

import config
import cores

from perguntas import perguntas

from components.advicetext import AdviceText
from components.versiontext import VersionText
from components.button import Button
from components.background import BackgroundImage
from components.forca import ForcaImage

from components.balaofala import BalaoFala

from components.perguntatext import PerguntaText
from components.respostatext import RespostaText

#os.environ['SDL_VIDEO_WINDOW_POS'] = "16,48"
class Game:
  def __init__(self):
    pg.init()
    self.clock = pg.time.Clock()
    pg.display.set_caption(config.TITLE)
    self.surface = pg.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    self.loop = True
    
    self.radomize_perguntas()
    
    self.scene = "menu"
    # self.start_game()
    
    pg.font.init()
    
    self.sons = {
      'digitar': pg.mixer.Sound("assets/sounds/digitar.wav")
    }
    
    self.fonts = {
      'smalltest': pg.font.SysFont('Inter', 20),
      'small': pg.font.SysFont('Inter', 24),
      'medium': pg.font.SysFont('Inter', 32),
      'large': pg.font.SysFont('Inter', 40),
      'title': pg.font.SysFont('Inter', 64),
      'largest': pg.font.SysFont('Inter', 72)
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
    
    self.restart_button = Button(
      x=config.WINDOW_WIDTH // 2 - 100, 
      y=config.WINDOW_HEIGHT // 2 - 25, 
      width=200, 
      height=50, 
      text="Reiniciar", 
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
    
    self.pergunta_text = PerguntaText(
      font_pergunta=self.fonts["small"],
      font_conjuntos=self.fonts["smalltest"]
    )
    
    self.resposta_text = RespostaText(
      font=self.fonts["largest"],
      resposta_font=self.fonts["medium"],
    )
    
    self.background_image_menu = BackgroundImage()   
    
    self.forca_image = ForcaImage()
     
    self.sapo_advogado_image = pg.image.load("assets/images/sapo_advogado.png").convert_alpha()      
    self.sapo_advogado_image = pg.transform.scale(self.sapo_advogado_image, (150, 466))
    
    self.background_image_game = pg.image.load("assets/images/game.jpg").convert()      
    self.background_image_game = pg.transform.scale(self.background_image_game, (config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    
    self.background_image_game_over = pg.image.load("assets/images/game_over.png").convert_alpha()      
    self.background_image_game_over = pg.transform.scale(self.background_image_game_over, (config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    
    self.game_balao = BalaoFala(
        x=config.WINDOW_WIDTH - 240 - 150 - 16, 
        y=config.WINDOW_HEIGHT // 2 - 208 - 16,  
        width=240, 
        height=208, 
        text="",
        font=self.fonts["largest"]
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
      elif event.type == pg.KEYDOWN:
        key = event.key
        self.valida_letra(pg.key.name(key))
        
    self.surface.fill(cores.WHITE)    
    
    if self.scene == "menu":
      self.menu()
    elif self.scene == "game":
      self.game()
    elif self.scene == "game_over":
      self.game_over()
    else:
      self.menu()
      
    self.version_text.draw(self.surface) 
    self.advice_text.draw(self.surface) 
    
    pg.display.flip()
    self.clock.tick(config.FPS)
    
  def radomize_perguntas(self):
    random.shuffle(perguntas)
    self.perguntas = perguntas
    
  def menu(self):      
    self.background_image_menu.draw(self.surface)
      
    title_text = self.fonts["title"].render("A FORCA", True, cores.BLACK)
    title_text_rect = title_text.get_rect(center=(config.WINDOW_WIDTH / 2, config.WINDOW_HEIGHT / 4))
    self.surface.blit(title_text, title_text_rect)      
        
    self.start_button.check_hover(self.mouse_pos)
    self.start_button.draw(self.surface)    
    if(self.start_button.is_clicked(self.mouse_pos, self.mouse_pressed)):
      self.radomize_perguntas()
      self.start_game()
      
  def start_game(self, pergunta_index = 0):
    self.pergunta_index = pergunta_index
    self.scene = "game"
    
    print(pergunta_index % len(self.perguntas))   
    self.pergunta = self.perguntas[pergunta_index % len(self.perguntas)]
    
    self.palavra = self.pergunta['palavra'].upper()
    
    self.ultima_letra = None
    self.ultima_letra_cor = cores.BLACK
    
    self.letras_restantes = list(self.palavra)
    self.letras_usadas = []
    self.erros = 0
    self.acertos = 0

  def valida_letra(self, letra):
    if self.erros >= 6 or self.acertos >= len(self.palavra):
      return
    
    letra = letra.upper()
    
    cor = cores.BLACK
    letra_aceita = False
    
    if letra.isalpha() and len(letra) == 1:
      letra_aceita = True
      if letra not in self.letras_usadas:
        self.letras_usadas.append(letra)
        
        if letra in self.letras_restantes:
          cor = cores.ACERTO
          self.letras_restantes = [char for char in self.letras_restantes if char != letra]
          self.acertos = (len(self.palavra) - len(self.letras_restantes))
        else:
          cor = cores.ERRO
          self.erros+=1
        
    if self.scene == "game" and letra_aceita:
      self.sons["digitar"].play()
      self.ultima_letra = letra
      self.ultima_letra_cor = cor
             
  def game(self):   
    self.surface.blit(self.background_image_game, (0, 0))
    self.surface.blit(self.sapo_advogado_image, (config.WINDOW_WIDTH - 150, config.WINDOW_HEIGHT - 466))
    
    you_text = self.fonts["small"].render("Sapu (Você)", True, cores.WHITE)
    you_text_rect = you_text.get_rect(bottomright=(config.WINDOW_WIDTH - 40, config.WINDOW_HEIGHT - 466 - 16))
    self.surface.blit(you_text, you_text_rect) 
    
    self.menu_button.check_hover(self.mouse_pos)
    self.menu_button.draw(self.surface)    
    if(self.menu_button.is_clicked(self.mouse_pos, self.mouse_pressed)):
      self.scene = "menu"
      
    self.forca_image.draw(self.surface, self.erros)
    
    letras_usadas_text = self.fonts["small"].render(f"Letras já usadas: {', '.join(self.letras_usadas)}", True, cores.BLACK)
    letras_usadas_text_rect = letras_usadas_text.get_rect(bottomleft=(24, config.WINDOW_HEIGHT - 48 - 6))
    pg.draw.rect(self.surface, cores.WHITE, (16, config.WINDOW_HEIGHT - 48 - 32, letras_usadas_text_rect.width + 16, 32))  
    self.surface.blit(letras_usadas_text, letras_usadas_text_rect) 

    if self.ultima_letra:
      self.game_balao.draw(
        surface=self.surface,
        text=self.ultima_letra.upper(),
        text_color=self.ultima_letra_cor
      )
      
    self.pergunta_text.draw(self.surface, self.pergunta)
    self.resposta_text.draw(self.surface, self.palavra, self.letras_usadas, self.erros)
    
    if self.erros >= 6 or self.acertos >= len(self.palavra):
      now_time = time.time()
      
      try:
        if(not self.last_time):
          self.last_time = now_time
      except:
        self.last_time = now_time
        
      if now_time - self.last_time > 5:
        if self.erros >= 6:
          self.scene = "game_over"
        else:
          self.start_game(self.pergunta_index + 1)
        self.last_time = None

  def game_over(self):
    self.surface.blit(self.background_image_game_over, (0, 0))
      
    title_text = self.fonts["title"].render("FIM DE JOGO", True, cores.BLACK)
    title_text_rect = title_text.get_rect(center=(config.WINDOW_WIDTH / 2, config.WINDOW_HEIGHT / 4))
    self.surface.blit(title_text, title_text_rect)      
        
    self.restart_button.check_hover(self.mouse_pos)
    self.restart_button.draw(self.surface)    
    if(self.restart_button.is_clicked(self.mouse_pos, self.mouse_pressed)):
      self.radomize_perguntas()
      self.start_game()
    
def main():
  game = Game()
  game.main()
  
main()