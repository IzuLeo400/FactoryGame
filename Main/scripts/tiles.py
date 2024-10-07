import pygame

NEIGHBOR_OFFSETS = [(-1, -1), (0, -1), (1, -1),
                    (-1, 0), (0, 0), (1, 0),
                    (-1, 1), (0, 1), (1, 1)]

class Tile:
    def __init__(self, pos, size, solid=True):
        self.pos = list(pos)
        self.size = size
        self.solid = solid
        self.img = pygame.surface.Surface((self.size, self.size))
        self.img.fill((30, 75, 220))

class Source(Tile):
  def __init__(self, pos, size, solid):
    super().__init__(pos, size, solid)

class Hydrogen(Source):
  def __init__(self, pos, size=16):
    super().__init__(pos, size, solid=False)
    self.img = pygame.Surface((self.size, self.size))
    self.img.fill((150, 50, 20))

class Oxygen(Source):
  def __init__(self, pos, size=16):
    super().__init__(pos, size, solid=False)
    self.img = pygame.Surface((self.size, self.size))
    self.img.fill((255, 180, 220))
        
class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        
        for i in range(8):
            self.tilemap[(3 + i, 8)] = Tile((3 + i, 8), self.tile_size)
            self.tilemap[(8, 3 + i)] = Tile((8, 3 + i), self.tile_size)
        self.tilemap[(-2, -3)] = Hydrogen((-2, -3), self.tile_size)
        self.tilemap[(-4, -1)] = Oxygen((-4, -1), self.tile_size)
    
    def point_to_loc(self, pos):
        return (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
            
    def loc_to_point(self, loc):
        return (loc[0] * self.tile_size, loc[1] * self.tile_size)

    def tiles_around(self, pos):
        tiles = []
        tile_loc = self.point_to_loc(pos)
        for offset in NEIGHBOR_OFFSETS:
            check_loc = (tile_loc[0] + offset[0], tile_loc[1] + offset[1])
            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])
        return tiles

    def physics_rects_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile.solid:
                rects.append(pygame.Rect(tile.pos[0] * self.tile_size, tile.pos[1] * self.tile_size, self.tile_size, self.tile_size))
        return rects
    
    def render(self, surface, offset=(0, 0)):
        for x in range(offset[0] // self.tile_size, (offset[0] + surface.get_width()) // self.tile_size + 1):
            for y in range(offset[1] // self.tile_size, (offset[1] + surface.get_height()) // self.tile_size + 1):
                location = (x, y)
                if location in self.tilemap:
                    tile = self.tilemap[(x, y)]
                    surface.blit(tile.img, (tile.pos[0] * self.tile_size - offset[0], tile.pos[1] * self.tile_size - offset[1]))    
