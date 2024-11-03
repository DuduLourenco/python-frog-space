import pygame as pg
import config
import cores

class RespostaText:  
    def __init__(self, font, resposta_font): 
      self.font = font  
      self.resposta_font = resposta_font   
  
    def draw(self, surface, palavra, letras_usadas, erros = 0):
      letras = list(palavra)
      text = ""
      text_color = cores.WHITE
      
      if erros >= 6:
        text_color = cores.ERRO
        
      acertos = 0
      
      for letra in letras:
        if letra in letras_usadas:
          text += letra + " "
          acertos += 1
        else:
          text += "_ " if letra != " " else "  "  
          
      if acertos >= len(palavra.replace(" ", "")):
        text_color = cores.ACERTO
      
      
      pergunta_text = self.font.render(text.strip(), True, text_color)
      pergunta_text_rect = pergunta_text.get_rect(center=(config.WINDOW_WIDTH // 2, config.WINDOW_HEIGHT - 160))
      surface.blit(pergunta_text, pergunta_text_rect)
      
      if acertos >= len(palavra.replace(" ", "")):
        next_pergunta_text = self.resposta_font.render(f"próxima pergunta em instantes...", True, cores.WHITE)
        next_pergunta_rect = next_pergunta_text.get_rect(center=(config.WINDOW_WIDTH // 2, config.WINDOW_HEIGHT - 112))
        surface.blit(next_pergunta_text, next_pergunta_rect)
      
      if erros >= 6:
        resposta_text = self.resposta_font.render(f"{''.join(letras)}", True, cores.WHITE)
        resposta_text_rect = resposta_text.get_rect(center=(config.WINDOW_WIDTH // 2, config.WINDOW_HEIGHT - 112))
        surface.blit(resposta_text, resposta_text_rect)
        
        time_text = self.resposta_font.render(f"game over em instantes...", True, cores.WHITE)
        time_text_rect = time_text.get_rect(center=(config.WINDOW_WIDTH // 2, config.WINDOW_HEIGHT - 80))
        surface.blit(time_text, time_text_rect)        
                
                
        
            
