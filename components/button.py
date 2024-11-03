import pygame as pg
import cores

class Button:
    def __init__(self, x, y, width, height, text, font, color_normal, color_hover):
        self.rect = pg.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.color_normal = color_normal
        self.color_hover = color_hover
        self.hovered = False
        self.last_click_time = 0  # Armazena o tempo do último clique

    def draw(self, surface):
        # Escolhe a cor com base no estado de hover
        color = self.color_hover if self.hovered else self.color_normal
        pg.draw.rect(surface, color, self.rect, border_radius=8)

        # Renderiza o texto no centro do botão
        text_surface = self.font.render(self.text, True, cores.BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        # Atualiza o estado de hover
        self.hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, mouse_pos, mouse_pressed):
        # Define um intervalo de clique (em milissegundos)
        click_interval = 300  # 300 milissegundos

        # Verifica se o botão foi clicado e se já passou o intervalo
        current_time = pg.time.get_ticks()
        if self.hovered and mouse_pressed[0] and (current_time - self.last_click_time >= click_interval):
            self.last_click_time = current_time
            return True
        return False