import pygame

class Cursor:

  def __init__(self, size=16):
    self.img = pygame.Surface((size, size))
    self.img.fill((160, 190, 50))
    self.size = size

  def render(self, surface, offset=(0, 0)):
    pos = pygame.mouse.get_pos()
    pos = (pos[0]/2, pos[1]/2)
    x_pos = (pos[0]+offset[0])//self.size
    y_pos = (pos[1]+offset[1])//self.size
    surface.blit(self.img, (x_pos * self.size - offset[0], y_pos * self.size - offset[1]))
    
    
