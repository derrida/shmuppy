import pygame
from constants import *

class Weapon(pygame.sprite.DirtySprite):
    """The base class that all weapons inherit from."""

    def __init__(self, size, color, speed):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.Surface(size).convert()
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.x = 10
        self.y = 10

    def draw(self):
        """Draw the weapon's new position."""

        self.dirty = 1
        #self.rect.move_ip([self.x * self.speed, self.y * self.speed])
        self.rect.center(player.x,player.y)

    def update(self):
        """Update the weapon's position on the screen."""

        if (self.x or self.y):
            self.draw()


class Bow(Arrow):
    """A Bow is a weapon that fires a single Arrow projectile."""

    def __init__(self):
        size = (2,4)
        color = (255,30,128)
        speed = 20
        Projectile.__init__(self, size, color, speed)
