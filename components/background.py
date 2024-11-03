import pygame as pg
import time

import config

class BackgroundImage:  
    def __init__(self):
      self.background_image_loaded = pg.image.load("assets/images/menu.jpg").convert()
      
      self.size_width = config.WINDOW_WIDTH
      self.size_height = config.WINDOW_HEIGHT
      
      self.background_image = pg.transform.scale(self.background_image_loaded, (self.size_width, self.size_height))
        
      self.last_time = time.time()
      self.multiplier_grow = 1.005
      self.multiplier_shrink = 0.80
      self.multiplier = self.multiplier_grow
    
    def invertImageColor(self):
      image = self.background_image_loaded  
      image = pg.transform.rotate(image, 180)    
      # for x in range(image.get_width()):
      #   for y in range(image.get_height()):
      #     r, g, b, a = image.get_at((x, y))  # Obtem os valores RGBA
      #     image.set_at((x, y), (255 - r, 255 - g, 255 - b, a))  # Inverte R, G, B
      for x in range(self.background_image_loaded.get_width()):
        for y in range(image.get_height()):
          r, g, b, a = image.get_at((x, y))  # Obtem os valores RGBA
          image.set_at((x, y), (r, g, 255 - b, a))  # Inverte R, G, B
      self.background_image_loaded = image
    
    def changeBackground(self):
      self.size_width = self.size_width * self.multiplier
      self.size_height = self.size_height * self.multiplier
      self.background_image = pg.transform.scale(self.background_image_loaded, (self.size_width, self.size_height))
      if self.size_width * self.multiplier > config.WINDOW_WIDTH * 2:
        self.multiplier = self.multiplier_shrink
        self.invertImageColor()
      elif self.size_width * self.multiplier < config.WINDOW_WIDTH:
        self.multiplier = self.multiplier_grow
        self.invertImageColor()
          
    def draw(self, surface):        
        now_time = time.time()
        if now_time - self.last_time > 1:
            self.last_time = now_time
            self.changeBackground()
            
        surface.blit(self.background_image, (0 - ((self.size_width - config.WINDOW_WIDTH) / 2), 0 - ((self.size_height- config.WINDOW_HEIGHT) / 2)))
