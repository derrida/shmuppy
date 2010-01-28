from random import randint
from sprite import Sprite
from projectiles import *

class Enemy(Sprite):
    """An enemy sprite."""

    def __init__(self, scene):
        self.scene = scene
        self.size = (24,24)
        self.color = (0,100,0)
        Sprite.__init__(self, self.size, self.color)
        self.speed = 1
        self.x = 0
        self.y = 0
        self.rect.move_ip(
            [ self.size[0] * randint(0, self.scene.room.num_tiles[0]),
            self.size[1] * randint(0, self.scene.room.num_tiles[1]) ])

    def move(self):
        """Move the enemy."""

        self.dirty = 1

    def die(self):
        """Check if an enemy is dead and kills it."""

        # If projectile hits enemy, kill enemy and projectile.
        for proj in self.scene.projectiles:
            if self.rect.colliderect(proj.rect):
                self.kill()
                proj.kill()

    def update(self):
        """Update the monster each frame."""

        if (self.x or self.y):
            self.move()
        self.die()
