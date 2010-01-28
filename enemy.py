from random import randint
from sprite import Sprite
from projectiles import *

class Enemy(Sprite):
    """An enemy sprite."""

    def __init__(self, scene):
        self.scene = scene
        self.size = (16,16)
        self.color = (0,100,0)
        Sprite.__init__(self, self.size, self.color)
        self.speed = 1
        self.x = 0
        self.y = 0
        self.rect.move_ip(
            [ self.size[0] * randint(0, self.scene.room.num_tiles[0]),
            self.size[1] * randint(0, self.scene.room.num_tiles[1]) ])

    def die(self):
        """Check if an enemy is dead and kills it."""

        for proj in self.scene.projs_player:
            if self.rect.colliderect(proj.rect):
                self.kill()
                proj.kill()

    def update(self):
        """Update the monster each frame."""

        if (self.x or self.y):
            Sprite.move(self)
        self.die()
