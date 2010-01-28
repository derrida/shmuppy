from random import randint
from sprite import Sprite
from projectiles import *

class Enemy(Sprite):
    """An enemy sprite."""

    def __init__(self, scene):
        self.scene = scene
        size = (16,16)
        color = (0,100,0)
        Sprite.__init__(self, size, color)
        self.rect.move_ip(
            [ size[0] * randint(0, self.scene.room.num_tiles[0]),
            size[1] * randint(0, self.scene.room.num_tiles[1]) ])

    def damaged(self):
        """Enemy is damaged."""

        pass

    def update(self):
        """Update the monster each frame."""

        if (self.x or self.y):
            Sprite.move(self)


class NameMe(Enemy):
    """Some unknown enemy yet to be named."""

    def __init__(self, scene):
        self.hp = [0,0]
        Enemy.__init__(self, scene)
