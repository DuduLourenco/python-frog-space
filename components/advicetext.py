import time
import random

import config
import cores

class AdviceText:  
    def __init__(self, font):
        self.texts = [
            "Quase nenhum sapo foi afetado durante o desenvolvimento desse jogo",
            "No campus da PUCPR de Curitiba existem aproximadamente 14 bilhões de sapos",
            "Esse jogo foi desenvolvido como projeto final de raciocínio matemático",
            "A pizzaria pítizza não patrocinou esse jogo",
            "Cuidado com o sapo mascarad... aaaaaaaaaaah croac-croac!"
        ]
        random.shuffle(self.texts)        
        self.text_index = 0    
        self.text = self.texts[self.text_index]
        self.font = font
        
        self.last_time = time.time()
        
    def changeText(self):
        self.text_index = (self.text_index + 1) % len(self.texts)
        self.text = self.texts[self.text_index]
  
    def draw(self, surface):        
        # Altera o texto a cada 10 segundos
        now_time = time.time()
        if now_time - self.last_time > 10:
            self.changeText()
            self.last_time = now_time
            
        # Cria a superfície do texto e posiciona
        text = self.font.render(self.text, True, cores.BLACK)
        text_rect = text.get_rect(bottomleft=(16, config.WINDOW_HEIGHT - 16))
        surface.blit(text, text_rect)
