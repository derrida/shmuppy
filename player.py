import pygame
from constants import *

class Player(pygame.sprite.DirtySprite):
    """The sprite that the player controls."""

    def __init__(self):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.Surface(PLAYER_SIZE).convert()
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0

    def draw(self):
        """Draw the player's new position if it changed."""

        self.dirty = 1
        self.rect.move_ip([self.x, self.y])
        self.rect.clamp_ip(SCREEN_RECT)

    def collide(self):
        """Check if the player collided with an object or screen edge."""

        move_rect = self.rect.move([self.x, self.y])
        collide = (300,400,24,24)
        if not SCREEN_RECT.contains(move_rect) or (
            Rect(move_rect).colliderect(collide)):
                return True

    def update(self):
        """Check the sprite for movement and collisions each frame."""

        if (self.x or self.y) and not self.collide():
            self.draw()
