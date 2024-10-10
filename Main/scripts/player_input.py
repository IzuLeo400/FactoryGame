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
            if event.key == pygame.K_x:
                self.movement[4] = True
            if event.key == pygame.K_c:
                self.movement[5] = True
            if event.key == pygame.K_q:
                self.movement[6] = True
            if event.key == pygame.K_e:
                self.movement[7] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.movement[0] = False
            if event.key == pygame.K_a:
                self.movement[1] = False
            if event.key == pygame.K_s:
                self.movement[2] = False
            if event.key == pygame.K_w:
                self.movement[3] = False
            if event.key == pygame.K_x:
                self.movement[4] = False
            if event.key == pygame.K_c:
                self.movement[5] = False
            if event.key == pygame.K_q:
                self.movement[6] = False
            if event.key == pygame.K_e:
                self.movement[7] = False