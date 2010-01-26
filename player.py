import pygame
from constants import *

class Player(pygame.sprite.DirtySprite):
    """The sprite that the player controls."""

    def __init__(self):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.Surface(PLAYER_SIZE).convert()
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.move_queue = []
        self.stop = True

    def move(self, moving, key):
        """Store and erase movement keys as they are pressed/released."""

        dir = KEYMAP[key]
        move_queue = self.move_queue
        if moving:
            self.stop = False
            move_queue.append(dir)
        else:
            if len(move_queue) > 0:
                if dir in move_queue:
                    del move_queue[move_queue.index(dir)]
            if len(move_queue) == 0:
                self.stop = True

    def draw(self):
        """Draw the player's new position if it changed."""

        # Set the player dirty for it to be rendered this frame
        self.dirty = 1

        # Move the player
        self.rect.move_ip(self.move_queue[-1])
        if len(self.move_queue) > 1:
            self.rect.move_ip(self.move_queue[-2])

        # Block the player from going outside of the screen
        self.rect.clamp_ip(SCREEN_RECT)

    def collide(self):
        """Check if the player collided with something."""

        move_rect = self.rect.move(self.move_queue[-1])
        collide = (300,400,24,24)
        return Rect(move_rect).colliderect(collide)

    def update(self):
        """Check the sprite for movement and collisions each frame."""

        if not self.stop:
            if not self.collide():
                self.draw()
            else:
                self.kill()
