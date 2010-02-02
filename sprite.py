from pygame import Surface
from pygame.sprite import DirtySprite

class Sprite(DirtySprite):
    """The base sprite class that all sprites inherit."""

    def __init__(self, scene, size, color):
        DirtySprite.__init__(self)
        self.scene = scene
        self.image = Surface(size).convert_alpha()
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.x, self.y = 0, 0
        self.facing = [0,2]

    def move(self):
        """Move the sprite and set it to dirty for the current frame."""

        self.dirty = 1
        self.rect.move_ip([self.x, self.y])

    def update(self):
        """Update the sprite each frame."""

        if (self.x or self.y):
            self.facing = [self.x, self.y]
            self.move()
            self.collide()
