import pygame
from constants import *
from projectiles import *

class Player(pygame.sprite.DirtySprite):
    """The sprite that the player controls."""

    def __init__(self):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.Surface(PLAYER_SIZE).convert()
        self.image.fill(ROOM_COLOR)
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, PLAYER_COLOR, self.rect.center, 12)
        self.x = 0
        self.y = 0

    def draw(self):
        """Draw the player's new position if it changed."""

        self.dirty = 1
        self.rect.move_ip([self.x, self.y])
        self.rect.clamp_ip(SCREEN_RECT)

    def collide(self):
        """Check if the player collided with an object or screen edge."""

        rect = self.rect.move([self.x, self.y])
        enemy_rects = []
        for enemy in self.game.enemies:
            enemy_rects.append(enemy.rect)
        if not SCREEN_RECT.contains(rect) or (
            Rect(rect).collidelistall(enemy_rects)):
                return True

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
            if not projectile.rect.colliderect(SCREEN_RECT):
                projectile.kill()
