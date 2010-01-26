import pygame
from constants import *

class Bullet(pygame.sprite.DirtySprite):
    """A Bullet is a single projectile."""

    def __init__(self):
        pygame.sprite.DirtySprite.__init__(self)
        self.dirty = 1
        self.image = pygame.Surface(BULLET_SIZE).convert()
        self.image.fill(BULLET_COLOR)
        self.rect = self.image.get_rect()

class Arrow(pygame.sprite.DirtySprite):
    """An Arrow is a single projectile."""

    def __init__(self):
        pygame.sprite.DirtySprite.__init__(self)
        self.dirty = 1
        self.image = pygame.Surface(ARROW_SIZE).convert()
        self.image.fill(ARROW_COLOR)
        self.rect = self.image.get_rect()

class Grenade(pygame.sprite.DirtySprite):
    """A Grenade is a single projectile."""

    def __init__(self):
        pygame.sprite.DirtySprite.__init__(self)
        self.dirty = 1
        self.image = pygame.Surface(GRENADE_SIZE).convert()
        self.image.fill(GRENADE_COLOR)
        self.rect = self.image.get_rect()

class Particle(pygame.sprite.DirtySprite):
    """A Particle is a single projectile."""

    def __init__(self):
        pygame.sprite.DirtySprite.__init__(self)
        self.dirty = 1
        self.image = pygame.Surface(PARTICLE_SIZE).convert()
        self.image.fill(PARTICLE_COLOR)
        self.rect = self.image.get_rect()
