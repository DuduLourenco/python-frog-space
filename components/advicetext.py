import config
import cores

import time

class AdviceText:  
  def __init__(self, font):
    self.texts = [
      "Quase nenhum sapo foi afetado durante o desenvolvimento desse jogo",
      "No campus da PUCPR de curitiba existem aproximadamente 14 bilhões de sapos",
      "Esse jogo foi desenvolvido como projeto final de raciocínio matemático"
    ]
    self.text_index = 0    
    self.text = self.texts[self.text_index]
    self.font = font
    
    self.last_time = time.time()
    
  def changeText(self):
    self.text_index = (self.text_index + 1) % len(self.texts)
    self.text = self.texts[self.text_index]
  
  def draw(self, surface):
    self.now_time = time.time()
    if self.now_time - self.last_time > 10:
      self.changeText()
      self.last_time = self.now_time
    
    text = self.font.render(self.text, True, cores.BLACK)
    text_rect = text.get_rect(bottomleft=(12, config.WINDOW_HEIGHT - 12))
    surface.blit(text, text_rect)