import pygame
from constants import *

class Projectile(pygame.sprite.DirtySprite):
    """The base that other projectiles inherit."""

    def __init__(self, size, color, speed):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.Surface(size).convert()
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.x = 0
        self.y = 0

    def draw(self):
        """Draw the projectile's new position."""

        self.dirty = 1
        self.rect.move_ip([self.x * self.speed, self.y * self.speed])

    def update(self):
        """Update the projectile on the screen."""

        if (self.x or self.y):
            self.draw()

class Bullet(Projectile):
    """A Bullet is a single projectile."""

    def __init__(self):
        size = (2,4)
        color = (255,0,128)
        speed = 6
        Projectile.__init__(self, size, color, speed)


class Arrow(Projectile):
    """A Arrow is a single projectile."""

    def __init__(self):
        size = (1,8)
        color = (128,128,0)
        speed = 4
        Projectile.__init__(self, size, color, speed)


class Grenade(Projectile):
    """A Grenade is a single projectile."""

    def __init__(self):
        size = (4,6)
        color = (255,120,50)
        speed = 1
        Projectile.__init__(self, size, color, speed)


class Particle(Projectile):
    """A Particle is a single projectile."""

    def __init__(self):
        size = (1,1)
        color = (255,255,255)
        speed = 2
        Projectile.__init__(self, size, color, speed)
