import pygame as pg
import config
import cores

class RespostaText:  
    def __init__(self, font): 
      self.font = font     
  
    def draw(self, surface, palavra, letras_usadas):
      letras = list(palavra)
      text = ""
      
      for letra in letras:
        if letra in letras_usadas:
          text += letra + " "
        else:
          text += "_ "
        
      
      pergunta_text = self.font.render(text.strip(), True, cores.WHITE)
      pergunta_text_rect = pergunta_text.get_rect(center=(config.WINDOW_WIDTH // 2, config.WINDOW_HEIGHT - 160))
      surface.blit(pergunta_text, pergunta_text_rect)
                
                
        
            
