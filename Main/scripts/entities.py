import pygame
import math

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
 
    def update(self, tilemap, movement=(0, 0)):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        
        frame_movement = (movement[0], movement[1])
        
        self.pos[0] += frame_movement[0]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entity_rect.x
        
        self.pos[1] += frame_movement[1]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = entity_rect.y
    
    def render(self, surf, offset=(0, 0)):
        player_img = pygame.surface.Surface(self.size)
        player_img.fill((255, 255, 255))
        surf.blit(player_img, (self.pos[0] - offset[0], self.pos[1] - offset[1]))

class Player(PhysicsEntity):
    def __init__(self, game, pos, size, zoom=1.0, rotation=0):
        super().__init__(game, "player", pos, size)
        self.zoom = zoom
        self.rotation = rotation

    def update(self, tilemap, movement=(0, 0, 0, 0, 0, 0, 0, 0)):
        super().update(tilemap, movement=((movement[0] - movement[1]), (movement[2] - movement[3])))
        self.zoom += ((movement[4] - movement[5]) * (0.1 * (self.zoom - 1)*(self.zoom - 1) + 0.3)) * 0.1
        if self.zoom > 5:
            self.zoom = 5
        elif self.zoom < -5:
            self.zoom = -5
        self.rotation += (movement[6] - movement[7]) 
