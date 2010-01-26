import pygame
from constants import *

class Room(pygame.sprite.DirtySprite):
    """A room is an area where a fight to the death takes place."""

    def __init__(self):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.Surface(RESOLUTION).convert()
        self.rect = self.image.get_rect()
        self.make_floor()

    def make_floor(self):
        """Create the room of floor tiles."""

        for y in range(0, ROOM_TILES[1] + 1):
            for x in range(0, ROOM_TILES[0] + 1):
                offset = (x * TILE_SIZE[0], y * TILE_SIZE[1])
                tile = FloorTile().image
                self.image.blit(tile, offset)


class FloorTile(pygame.sprite.DirtySprite):
    """A room is made up of many floor tiles."""

    def __init__(self):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.Surface(TILE_SIZE).convert()
        self.image.fill(ROOM_COLOR)
        self.rect = self.image.get_rect()
        if SHOW_DEBUG:
            offset = self.rect.move([-1,-1])
            pygame.draw.rect(self.image, GRID_COLOR, offset, 1)
