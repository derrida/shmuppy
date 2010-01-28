from sprite import Sprite
from projectiles import *
import config

class Player(Sprite):
    """The sprite that the player controls."""

    def __init__(self, scene):
        self.scene = scene
        self.screen = scene.screen
        size = (16,16)
        color = (100,0,0)
        self.speed = 2
        self.hp = [0,0]
        Sprite.__init__(self, size, color)

    def die(self):
        """Check if player died."""

        for proj in self.scene.projs_enemy:
            if self.rect.colliderect(proj.rect):
                self.scene.projs.kill()
                self.kill()

    def shoot(self):
        """Shoot a projectile."""

        proj = Grenade(self.scene)
        self.scene.projs_player.add(proj)
        self.scene.projs.add(self.scene.projs_player)
        self.scene.all.add(self.scene.projs)
        proj.rect.x = self.rect.centerx + (6 * self.facing[0])
        proj.rect.y = self.rect.centery + (6 * self.facing[1])
        proj.x = self.facing[0]
        proj.y = self.facing[1]

    def next_weapon(self):
        """Switch the player's weapon to the next weapon in their inventory."""

        pass

    def update(self):
        """Update the player each frame."""

        if (self.x or self.y):
            Sprite.face(self)
            Sprite.move(self)
        self.die()
