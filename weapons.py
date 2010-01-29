from sprite import Sprite
from projectiles import *

class Weapon(Sprite):
    """The base class that all weapons inherit from."""

    def __init__(self, size, color, firing_rate, ammo_type):
        Sprite.__init__(self, size)
        self.firing_rate = firing_rate
        self.ammo_type = ammo_type

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
        self.size = (2,4) # size of weapon graphic
        self.color = (25,166,192) # temporary color
        self.speed = 20 # weapon's rate of fire
        self.fire_rate = 2
        self.ammo_type = Arrow
        Weapon.__init__(self, self.size, self.color, self.fire_rate, self.ammo_type)



class Pistol(Weapon):
  """A Pistol is a weapon that fires a single Bullet projectile"""

  def __init__(self):
    self.size = (2,4) 
    self.color = (0, 140, 240)
    self.speed = 10
    self.fire_rate = 1
    self.ammo_type = Bullet
    Weapon.__init__(self, self.size, self.color, self.fire_rate, self.ammo_type)
