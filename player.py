from pygame import Surface, Rect
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
        self.speed = 3
        self.x = 0
        self.y = 0

    def move(self):
        """Move the player."""

        Sprite.move(self)
        self.rect.clamp_ip(self.screen.get_rect())

    def collide(self):
        """Check if the player collided with an object or screen edge."""

        rect = self.rect.move([self.x, self.y])
        enemy_rects = []
        for enemy in self.scene.enemies:
            enemy_rects.append(enemy.rect)
        if not self.screen.get_rect().contains(rect) or (
            Rect(rect).collidelistall(enemy_rects)): return True

    def shoot(self):
        """Shoot a projectile."""

        proj = Arrow(self.scene)
        self.scene.projectiles.add(proj)
        self.scene.all.add(self.scene.projectiles)
        proj.rect.x = self.rect.centerx
        proj.rect.y = self.rect.centery
        proj.y = 1

    def update(self):
        """Update the player each frame."""

        # Draw the player at its new position.
        if (self.x or self.y) and not self.collide():
            self.move()
