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
        self.image.fill(BGCOLOR)
        self.rect = self.image.get_rect()


class Player(pygame.sprite.DirtySprite):
    """The sprite that the player controls."""

    def __init__(self):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.Surface(PLAYER_SIZE).convert()
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.move_queue = []
        self.stop = True

    def move(self, moving, key):
        """Store and erase movement keys as they are pressed/released."""

        dir = KEYMAP[key]
        move_queue = self.move_queue
        if moving:
            move_queue.append(dir)
            self.stop = False
        else:
            if len(move_queue) > 0:
                if dir in move_queue:
                    del move_queue[move_queue.index(dir)]
            if len(move_queue) == 0:
                self.stop = True

    def draw(self, dir):
        """Controls key input to the player character."""

        self.dirty = 1
        self.rect.move_ip(dir)

    def update(self):
        """Draw the sprite's new position."""

        if not self.stop:
            self.draw(self.move_queue[-1])
            if len(self.move_queue) > 1:
                self.draw(self.move_queue[-2])
            self.rect.clamp_ip(SCREEN_RECT)


class Enemy(pygame.sprite.DirtySprite):
    """An enemy sprite."""

    def __init__(self):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.Surface(ENEMY_SIZE).convert()
        self.image.fill(ENEMY_COLOR)
        self.rect = self.image.get_rect()
        self.rect.move_ip(ENEMY_POSITION)
