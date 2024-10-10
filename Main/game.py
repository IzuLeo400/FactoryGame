import pygame

from scripts.player_input import update as player_input
from scripts.entities import Player
from scripts.tiles import Tilemap

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Platformer")
        self.screen = pygame.display.set_mode((1280, 960))
        self.display = pygame.Surface((640, 480))

        self.clock = pygame.time.Clock()
        
        self.assets = {}
        
        self.player = Player(self, (100, 0), (16, 16), 1.0, 0.0)

        self.tilemap = Tilemap(self)

        #axis scroll =  X, Y, Z, R (X: -infinity -> 0 -> infinity, Y: -infinity -> 0 -> infinity, Z: -infinity -> 1 -> infinity, R: 0 -> 360; (0 -> +x_axis, + -> counter_clockwise))
        self.scroll  = [0, 0, 1, 0]

        #key movement -> D =+x, A =-x  S =+y, W =-y, X =+z, C =-z, Q =+r, E =+r
        self.movement = [False, False, False, False, False, False, False, False]

    def run(self):
        while True:
            self.game_loop()

    def game_loop(self):
        self.display.fill((0, 0, 0))

        player_input(self)

        self.player.update(self.tilemap, self.movement)

        self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 20
        self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 20
        self.scroll[2] += (self.player.zoom - self.scroll[2]) / 20
        self.scroll[3] += (self.player.rotation - self.scroll[3]) / 20
        print(self.scroll[3])
        render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

        self.tilemap.render(self.display, render_scroll)
        self.player.render(self.display, render_scroll)

        self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
        pygame.display.update()
        self.clock.tick(60)

Game().run()