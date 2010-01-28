from sprite import Sprite
from projectiles import *
import config

class Player(Sprite):
    """The sprite that the player controls."""

    def __init__(self, scene):
        self.scene = scene
        self.screen = scene.screen
        size = (24,24)
        color = (100,0,0)
        Sprite.__init__(self, size, color)
        self.speed = 2
        self.x = 0
        self.y = 0

    def die(self):
        """Check if player died."""

        for proj in self.scene.projs_enemy:
            if self.rect.colliderect(proj.rect):
                self.scene.projs.kill()
                self.kill()

    def shoot(self):
        """Shoot a projectile."""

        proj = Bullet(self.scene)
        self.scene.projs_player.add(proj)
        self.scene.projs.add(self.scene.projs_player)
        self.scene.all.add(self.scene.projs)
        proj.rect.x = self.rect.centerx
        proj.rect.y = self.rect.centery + 6
        proj.y = 1

    def update(self):
        """Update the player each frame."""

        if (self.x or self.y) and not self.collide(self.scene):
            Sprite.move(self)
        self.die()

    def next_weapon(self):
        """Switch the player's weapon to the next weapon in their inventory."""
