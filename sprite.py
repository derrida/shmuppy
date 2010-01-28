from pygame import Surface
from pygame.sprite import DirtySprite

class Sprite(DirtySprite):
    """The base sprite class that all sprites inherit."""

    def __init__(self, size, color=(0,0,0)):
        DirtySprite.__init__(self)
        self.image = Surface(size).convert()
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.facing = (0,1)
        self.face()

    def face(self):
        """Face the sprite in the direction it's moving in."""

        if (self.x or self.y):
            self.facing = (self.x, self.y)

    def move(self):
        """Move the sprite and set it to dirty for the current frame."""

        self.dirty = 1
        self.rect.move_ip([self.x, self.y])
        self.rect.clamp_ip(self.scene.screen.get_rect())
