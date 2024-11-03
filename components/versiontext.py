import config
import cores

class VersionText:  
    def __init__(self, font): 
        self.text = config.VERSION
        self.font = font       
  
    def draw(self, surface):
        version_text = self.font.render(config.VERSION, True, cores.BLACK)
        version_text_rect = version_text.get_rect(bottomright=(config.WINDOW_WIDTH - 16, config.WINDOW_HEIGHT - 16))
        surface.blit(version_text, version_text_rect) 
