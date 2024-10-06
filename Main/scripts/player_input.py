import pygame
import sys

def update(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.movement[0] = True
            if event.key == pygame.K_a:
                self.movement[1] = True
            if event.key == pygame.K_s:
                self.movement[2] = True
            if event.key == pygame.K_w:
                self.movement[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.movement[0] = False
            if event.key == pygame.K_a:
                self.movement[1] = False
            if event.key == pygame.K_s:
                self.movement[2] = False
            if event.key == pygame.K_w:
                self.movement[3] = False