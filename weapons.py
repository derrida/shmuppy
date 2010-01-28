from sprite import Sprite

class Weapon(Sprite):
    """The base class that all weapons inherit from."""

    def __init__(self, size, color, speed):
        Sprite.__init__(self)
        self.speed = speed

    def move(self):
        """Draw the weapon's new position."""

        self.dirty = 1
        self.rect.center(player.x, player.y)




class Bow(Weapon):
    """A Bow is a weapon that fires a single Arrow projectile."""

    def __init__(self):
        size = (2,4) # size of weapon graphic
        color = (25,166,192) # temporary color
        speed = 20 # weapon's rate of fire
        Weapon.__init__(self, size, color, speed)
