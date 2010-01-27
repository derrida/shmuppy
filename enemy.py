import random
from pygame.sprite import DirtySprite
from pygame import Surface, Rect
from projectiles import *

class Enemy(DirtySprite):
    """An enemy sprite."""

    def __init__(self, room):
        DirtySprite.__init__(self)
        color = (0,100,0)
        size = (24,24)
        self.image = Surface(size).convert()
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.move_ip(
            [ size[0] * random.randint(0, room.num_tiles[0]),
            size[1] * random.randint(0, room.num_tiles[1]) ])

    def update(self):

        # Kill any enemies that are hit by a projectile
        for proj in self.game.projectiles:
            if Rect(self.rect).colliderect(proj.rect):
                self.kill()
                proj.kill()
