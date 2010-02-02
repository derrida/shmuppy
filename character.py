from pygame import time
from sprite import Sprite
import config
import random
#from random import Random

class Character(Sprite):
    """A player or enemy character."""



    def __init__(self, scene, size, color, name, speed, hp):
        Sprite.__init__(self, scene, size, color)
        self.name = name
        self.speed = speed
        self.hp = hp
        self.weapon_id = 0
        self.weapon = scene.weapon_list[self.weapon_id]
        self.firing = False
        self.last_fired = 0

    def collide(self):
        """Check if the character collides with something."""

        # If character hits a screen edge, stop it.
        self.rect.clamp_ip(self.scene.screen.get_rect())

    def fire_weapon(self):
        """Fire the character's weapon."""

        last_fired = self.last_fired + self.weapon.fire_rate * 100
        if last_fired < time.get_ticks():
            self.weapon.fire()
            self.last_fired = time.get_ticks()

    def damage(self, amount):
        """Damage an enemy."""

        self.damage_is = amount - (amount*random.random())


        if self.hp > 0:
            self.hp -= self.damage_is
        else:
            self.die()

        if config.DEBUG:
            print "%s was hit for %s damage!" % (self.name, self.damage_is)

    def die(self):
        """The enemy is killed."""

        # TODO: Put death animation here
        self.kill()

    def update(self):
        """Update the character each frame."""

        # If the characters shoots, shoot but only when its weapon is reloaded.
        # optional ideas: player can hit a key during reload period to gain a
        #                 save from the wait penalty (instant reload).
        if self.firing:
            self.fire_weapon()

        # Update the character's graphic.
        Sprite.update(self)
