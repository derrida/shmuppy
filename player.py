from sprite import Sprite
from projectiles import *
from weapons import *

class Player(Sprite):
    """The sprite that the player controls."""

    def __init__(self, scene):
        self.scene = scene
        self.screen = scene.screen
        size = (16,16)
        color = (100,0,0)
        self.speed = 2
        self.hp = [0,0]
        self.weapon = 0
        self.weapons = [Pistol(), Bow()]
        Sprite.__init__(self, size, color)

    def damage(self):
        """Player is damaged."""

        pass

    def shoot(self):
        """Shoot a projectile."""

        #proj = Grenade(self.scene)
        proj = self.weapons[self.weapon].ammo_type(self.scene)
        self.scene.projs_player.add(proj)
        self.scene.projs.add(self.scene.projs_player)
        self.scene.all.add(self.scene.projs)
        proj.rect.x = self.rect.centerx + (6 * self.facing[0])
        proj.rect.y = self.rect.centery + (6 * self.facing[1])
        proj.x = self.facing[0]
        proj.y = self.facing[1]


    def add_weapon(self, weapon):
      """Add a weapon to the player's inventory"""
      self.weapons += weapon
    def next_weapon(self):
        """Switch the player's weapon to the next weapon in their inventory."""
        if (self.weapon == len(self.weapons) -1): 
                #We are at the end of the inventory
                self.switch_weapon(0)
        else:
                self.switch_weapon(self.weapon+1)
              

    def switch_weapon(self, number):
      """Switch to a given weapon in the player's inventory"""
      self.weapon = number

