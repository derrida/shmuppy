from pygame.sprite import DirtySprite
from pygame import Surface

class Weapon(DirtySprite):
    """The base class that all weapons inherit from."""

    def __init__(self, size, color, speed):
        DirtySprite.__init__(self)
        self.image = Surface(size).convert()
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.x = 0
        self.y = 0

    def move(self):
        """Draw the weapon's new position."""

        self.dirty = 1
        self.rect.center(player.x, player.y)

    def update(self):
        """Update the weapon each frame."""

        if (self.x or self.y):
            self.move()


class Bow(Weapon):
    """A Bow is a weapon that fires a single Arrow projectile."""

    def __init__(self):
        size = (2,4) # size of weapon graphic
        color = (25,166,192) # temporary color
        speed = 20 # weapon's rate of fire
        Weapon.__init__(self, size, color, speed)
