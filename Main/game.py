import pygame

from scripts.player_input import update as player_input
from scripts.entities import Player
from scripts.tiles import Tilemap


class Game:

    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Factory Game")
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        self.assets = {}

        self.player = Player(self, (100, 0), (16, 16))

        self.tilemap = Tilemap(self)

        self.scroll = [0, 0]

        self.movement = [False, False, False, False]

    def run(self):
        while True:
            self.game_loop()

    def game_loop(self):
        self.display.fill((100, 3, 7))

        player_input(self)

        self.player.update(self.tilemap, self.movement)

        self.scroll[0] += (self.player.rect().centerx -
                           self.display.get_width() / 2 - self.scroll[0]) / 20
        self.scroll[1] += (self.player.rect().centery -
                           self.display.get_height() / 2 - self.scroll[1]) / 20
        render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

        self.tilemap.render(self.display, render_scroll)
        self.player.render(self.display, render_scroll)

        self.screen.blit(
            pygame.transform.scale(self.display, self.screen.get_size()),
            (0, 0))
        pygame.display.update()
        self.clock.tick(60)


Game().run()
