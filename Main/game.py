import pygame

from scripts.player_input import update as player_input
from scripts.entities import Player
from scripts.tiles import Tilemap
from scripts.controls import Cursor
from scripts.sprites import load_image, load_images, Animation


class Game:

    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Factory Game")
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()
        
        self.assets = {
            "Cursor": load_image('PlayerControls/Cursor.png'),
            "Sources": {
                "HydrogenSource": load_image('Sources/HydrogenSource.png'),
                "OxygenSource": load_image('Sources/OxygenSource.png')
            },
            "Tiles": {
                "Wall": load_image('Tiles/Wall.png')
            },
            "Player": {
                "Idle": load_image('Player/Idle.png')
            }
        }

        self.player = Player(self, (100, 0), (16, 16))

        self.tilemap = Tilemap(self)

        self.cursor = Cursor(self.assets["Cursor"], size=16)

        self.scroll = [0.0, 0.0]

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
        self.cursor.render(self.display, render_scroll)
        self.player.render(self.display, render_scroll)

        self.screen.blit(
            pygame.transform.scale(self.display, self.screen.get_size()),
            (0, 0))
        pygame.display.update()
        self.clock.tick(60)


Game().run()
