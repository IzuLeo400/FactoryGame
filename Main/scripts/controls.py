import pygame


class Cursor:

  def __init__(self, img, size=16):
    self.img = img
    self.size = size
    self.x_pos = 0
    self.y_pos = 0

  def render(self, surface, offset=(0, 0)):
    pos = pygame.mouse.get_pos()
    pos = (pos[0] / 2, pos[1] / 2)
    self.x_pos = (pos[0] + offset[0]) // self.size
    self.y_pos = (pos[1] + offset[1]) // self.size
    surface.blit(self.img, (self.x_pos * self.size - offset[0], self.y_pos * self.size - offset[1]))