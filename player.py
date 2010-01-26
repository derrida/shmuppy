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

        # Set the player dirty for it to be rendered this frame
        self.dirty = 1

        # Move the player
        self.rect.move_ip([self.x, self.y])

        # Block the player from going outside of the screen
        self.rect.clamp_ip(SCREEN_RECT)

    def collide(self):
        """Check if the player collided with something."""

        move_rect = self.rect.move([self.x, self.y])
        collide = (300,400,24,24)
        return Rect(move_rect).colliderect(collide)

    def update(self):
        """Check the sprite for movement and collisions each frame."""

        if not self.collide():
            self.draw()
