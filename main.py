import pygame as pg

import os

import config
import cores

from components.advicetext import AdviceText
from components.versiontext import VersionText
from components.button import Button
from components.background import BackgroundImage
from components.forca import ForcaImage

from components.balaofala import BalaoFala
from components.perguntatext import PerguntaText

os.environ['SDL_VIDEO_WINDOW_POS'] = "16,48"

conjuntos = [
  {
    'nome': 'Conjunto de pessoas que gostam de música clássica',
    'valores': ['Ana','Bruno','Carla','Daniel']
  },
  {
    'nome': 'Conjunto de pessoas que gostam de jazz',
    'valores': ['Bruna','Eduarda','Fabio','Gabriela']
  },
  {
    'nome': 'Conjunto de pessoas que gostam de rock',
    'valores': ['Ana','Gabriela','Hector','Isabel']
  },
  {
    'nome': 'Conjunto de pessoas que gostam de música eletrônica',
    'valores': ['Carla','Eduarda','Isabel','Joao']
  }
]

perguntas = [
  {
    'pergunta': 'Quem gosta de música clássica e jazz ao mesmo tempo?',
    'palavra': 'Bruno',
    'conjuntos': conjuntos
  },
  {
    'pergunta': 'Quem gosta de música clássica ou jazz?',
    'palavra': 'Ana',
    'conjuntos': conjuntos
  },
  {
    'pergunta': 'Quem gosta apenas de música clássica, mas não jazz?',
    'palavra': 'Daniel',
    'conjuntos': conjuntos
  },
  {
    'pergunta': 'Quem gosta de rock e não gosta de música eletrônica?',
    'palavra': 'Hector',
    'conjuntos': conjuntos
  },
  {
    'pergunta': 'Quem gosta de música eletrônica ou jazz, mas não de música clássica?',
    'palavra': 'Eduarda',
    'conjuntos': conjuntos
  }
]

class Game:
  def __init__(self):
    pg.init()
    self.clock = pg.time.Clock()
    pg.display.set_caption(config.TITLE)
    self.surface = pg.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    self.loop = True
    
    # self.scene = "menu"
    self.start_game()
    
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
    
    self.background_image_menu = BackgroundImage()   
    
    self.forca_image = ForcaImage()
     
    self.sapo_advogado_image = pg.image.load("assets/images/sapo_advogado.png").convert_alpha()      
    self.sapo_advogado_image = pg.transform.scale(self.sapo_advogado_image, (150, 466))
    
    self.background_image_game = pg.image.load("assets/images/game.jpg").convert()      
    self.background_image_game = pg.transform.scale(self.background_image_game, (config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    
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
    else:
      self.menu()
      
    self.version_text.draw(self.surface) 
    self.advice_text.draw(self.surface) 
    
    pg.display.flip()
    self.clock.tick(config.FPS)
    
  def menu(self):      
    self.background_image_menu.draw(self.surface)
      
    title_text = self.fonts["title"].render("A FORCA", True, cores.BLACK)
    title_text_rect = title_text.get_rect(center=(config.WINDOW_WIDTH / 2, config.WINDOW_HEIGHT / 4))
    self.surface.blit(title_text, title_text_rect)      
        
    self.start_button.check_hover(self.mouse_pos)
    self.start_button.draw(self.surface)    
    if(self.start_button.is_clicked(self.mouse_pos, self.mouse_pressed)):
      self.start_game()
      
  def start_game(self):
    self.scene = "game"
    
    self.pergunta = perguntas[0]
    
    self.palavra = self.pergunta['palavra']
    
    self.ultima_letra = None
    self.ultima_letra_cor = cores.BLACK
    
    self.letras_restantes = list(self.palavra)
    self.letras_usadas = []
    self.erros = 0
  
  def valida_letra(self, letra):
    print(f'letras_usadas -> {self.letras_usadas}')
    print(f'erros -> {self.erros}')
    print(f'valida_letra({letra}) -> isalpha: {letra.isalpha()}, acerto: {letra in self.letras_restantes}')
    
    cor = cores.BLACK
    letra_aceita = False
    
    if letra.isalpha() and len(letra) == 1:
      letra_aceita = True
      if letra not in self.letras_usadas:
        self.letras_usadas.append(letra)
        
        if letra in self.letras_restantes:
          cor = cores.ACERTO
          self.letras_restantes = [char for char in self.letras_restantes if char != letra]
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
      
    self.forca_image.draw(self.surface)
    
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

def main():
  game = Game()
  game.main()
  
main()