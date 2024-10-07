import pygame


class Cursor:

  def __init__(self, size=16):
    self.img = pygame.Surface((size, size))
    self.img.fill((160, 190, 50, 100))
    self.size = size

  def render(self, mouse_pos):
    pass
