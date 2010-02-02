from random import randint, choice
from pygame import display
from pygame.sprite import Group, LayeredDirty
from room import Room
from player import Player
from enemy import *
from weapons import *

class Scene(object):

    def __init__(self, screen):
        """Create the scene's objects."""

        self.screen = screen
        self.running = True

        # Groups for sprites
        self.players = Group()
        self.enemies = Group()
        self.chars = Group()
        self.weapons = Group()
        self.projs = Group()
        self.all = LayeredDirty()

        # Room
        self.room = Room(self)
        self.all.add(self.room)

        # Weapons
        self.weapon_list = [ LaserGun(self), Bow(self) ]
        for weapon in self.weapon_list:
            self.weapons.add(weapon)

        # Players
        self.player = Player(self)
        self.players.add(self.player)
        self.all.add(self.players)

        # Enemies
        enemy_list = [ Human, Glork ]
        for enemy in range(0, randint(50,100)):
            self.enemies.add(choice(enemy_list)(self))
        self.all.add(self.enemies)

        # Characters
        self.chars.add([self.players, self.enemies])

        # Layers
        self.all = LayeredDirty([
            self.room,
            self.enemies,
            self.players,
            self.weapons,
            self.projs ])

    def draw(self):
        """Draw all of the objects to the screen."""

        # Update all scene layers to the screen.
        self.all.update()
        self.dirty_rects = self.all.draw(self.screen)
        display.update(self.dirty_rects)
