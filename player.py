from pygame.sprite import DirtySprite
from pygame import Surface, Rect
from projectiles import *
import config

class Player(DirtySprite):
    """The sprite that the player controls."""

    def __init__(self, screen):
        DirtySprite.__init__(self)
        self.screen = screen
        color = (100,0,0)
        size = (24,24)
        self.image = Surface(size).convert()
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = 3
        self.x = 0
        self.y = 0

    def draw(self):
        """Draw the player's new position if it changed."""

        self.dirty = 1
        self.rect.move_ip([self.x, self.y])
        self.rect.clamp_ip(self.game.screen.get_rect())

    def collide(self):
        """Check if the player collided with an object or screen edge."""

        rect = self.rect.move([self.x, self.y])
        enemy_rects = []
        for enemy in self.game.enemies:
            enemy_rects.append(enemy.rect)
        if not self.screen.get_rect().contains(rect) or (
            Rect(rect).collidelistall(enemy_rects)): return True

    def shoot(self):
        """Shoot a projectile."""

        proj = Arrow()
        self.game.projectiles.add(proj)
        self.game.all.add(self.game.projectiles)
        proj.rect.x = self.rect.centerx
        proj.rect.y = self.rect.centery
        proj.y = 1

    def update(self):
        """Check the sprite for movement and collisions each frame."""

        # Draw the player at its new position.
        if (self.x or self.y) and not self.collide():
            self.draw()

        # Remove any projectiles that go off screen.
        for projectile in self.game.projectiles:
            if not projectile.rect.colliderect(self.screen.get_rect()):
                projectile.kill()
