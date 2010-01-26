import pygame
from constants import *

class Projectile(pygame.sprite.DirtySprite):
    """The base that other projectiles inherit."""

    def __init__(self, size, color):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.Surface(size).convert()
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def update(self):
        self.dirty = 1


class Bullet(Projectile):
    """A Bullet is a single projectile."""

    def __init__(self):
        Projectile.__init__(self, (2,4), (255,0,128))


class Arrow(Projectile):
    """A Arrow is a single projectile."""

    def __init__(self):
        Projectile.__init__(self, (1,8), (128,0,255))


class Grenade(Projectile):
    """A Grenade is a single projectile."""

    def __init__(self):
        Projectile.__init__(self, (4,6), (128,255,128))


class Particle(Projectile):
    """A Particle is a single projectile."""

    def __init__(self):
        Projectile.__init__(self, (1,1), (255,128,0))
