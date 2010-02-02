from pygame import time
from sprite import Sprite
from projectiles import *

class Weapon(Sprite):
    """The base class that all weapons inherit from."""

    def __init__(self, scene, size, color, fire_rate, ammo_type, ammo_max):
        Sprite.__init__(self, scene, size, color)
        self.fire_rate = fire_rate
        self.ammo_type = ammo_type
        self.ammo_max = ammo_max
        self.ammo_count = ammo_max

    def fire(self):
        """Fire one projectile of the weapon's selected ammo type."""

        if self.ammo_count:
           self.ammo_type(self.scene)
           self.ammo_count -= 1


class Bow(Weapon):
    """A Bow is a weapon that fires a single Arrow projectile."""

    def __init__(self, scene):
        size = (2,4)
        color = (25,166,192)
        fire_rate = 10
        ammo_type = Arrow
        ammo_max = 20
        Weapon.__init__(self, scene, size, color, fire_rate, ammo_type,
            ammo_max)


class LaserGun(Weapon):
    """A Pistol is a weapon that fires a single Bullet projectile"""

    def __init__(self, scene):
        size = (2,4)
        color = (0, 140, 240)
        fire_rate = 0
        ammo_type = Laser
        ammo_max = 200
        Weapon.__init__(self, scene, size, color, fire_rate, ammo_type,
            ammo_max)

class Particle_Rifle(Weapon):
    """A Rifle that can fire either a sigle particle projectile or a
       burst of 7-(7*<Character Level>)"""

    def __init__(self, scene):
        size = (3,3)
        color = (230, 90, 240)
        fire_rate = 15
        ammo_type = Particle
        ammo_max = 200
        Weapon.__init__(self, scene, size, color, fire_rate, ammo_type,
            ammo_max)
