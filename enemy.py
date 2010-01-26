import random
import pygame
from constants import *

class Enemy(pygame.sprite.DirtySprite):
    """An enemy sprite."""

    def __init__(self):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.Surface(ENEMY_SIZE).convert()
        self.image.fill(ROOM_COLOR)
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, ENEMY_COLOR, self.rect.center, 12)
        self.rect.move_ip(
            [ ENEMY_SIZE[0] * random.randint(0, ROOM_TILES[0]),
            ENEMY_SIZE[1] * random.randint(0, ROOM_TILES[1]) ])

    def update(self):

        # Kill any enemies that are hit by a projectile
        for proj in self.game.projectiles:
            if Rect(self.rect).colliderect(proj.rect):
                self.kill()
                proj.kill()
