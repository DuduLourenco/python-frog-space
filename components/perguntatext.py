import pygame as pg
import config
import cores
import string

alfabeto = list(string.ascii_uppercase)

class PerguntaText:  
    def __init__(self, font_pergunta, font_conjuntos): 
        self.font_pergunta = font_pergunta
        self.font_conjunto = font_conjuntos      
  
    def draw(self, surface, pergunta):       
        x = 28
        y = 26
        pergunta_text = self.font_pergunta.render(pergunta['pergunta'], True, cores.BLACK)
        pergunta_text_rect = pergunta_text.get_rect(topleft=(x, y))
        pg.draw.rect(surface, cores.WHITE, (16, 16, pergunta_text_rect.width + 32, pergunta_text_rect.height + 16)) 
        surface.blit(pergunta_text, pergunta_text_rect)
        
        if 'conjuntos' in pergunta:
            y += pergunta_text_rect.height + 16
            for index, conjunto in enumerate(pergunta["conjuntos"]): 
                letra_alfabeto = alfabeto[index]
                text_nome = f"Conjunto {letra_alfabeto}: {conjunto['nome']}:"               
                conjunto_nome_text = self.font_conjunto.render(text_nome, True, cores.BLACK)
                conjunto_nome_text_rect = conjunto_nome_text.get_rect(topleft=(x, y + 5))
                pg.draw.rect(surface, cores.WHITE, (16, y, conjunto_nome_text_rect.width + 32, conjunto_nome_text_rect.height + 8)) 
                surface.blit(conjunto_nome_text, conjunto_nome_text_rect)
                y += conjunto_nome_text_rect.height + 4
                
                text_valores = letra_alfabeto + " = {" + ', '.join(conjunto["valores"]) + "}"
                conjunto_valores_text = self.font_conjunto.render(text_valores, True, cores.BLACK)
                conjunto_valores_text_rect = conjunto_valores_text.get_rect(topleft=(x, y + 5))
                pg.draw.rect(surface, cores.WHITE, (16, y, conjunto_valores_text_rect.width + 32, conjunto_valores_text_rect.height + 8)) 
                surface.blit(conjunto_valores_text, conjunto_valores_text_rect)
                y += conjunto_valores_text_rect.height + 16
                
                
        
            
