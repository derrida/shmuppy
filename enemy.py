import pygame
from constants import *

class Enemy(pygame.sprite.DirtySprite):
    """An enemy sprite."""

    def __init__(self):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.Surface(ENEMY_SIZE).convert()
        self.image.fill(ENEMY_COLOR)
        self.rect = self.image.get_rect()
        self.rect.move_ip(ENEMY_POSITION)
