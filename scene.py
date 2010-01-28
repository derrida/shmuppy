from random import randint
from pygame import display
from pygame.sprite import Group, LayeredDirty
from room import Room
from player import Player
from enemy import *

class Scene(object):

    def __init__(self, screen):
        """Create the scene's objects."""

        # The screen created at startup that we will draw to.
        self.screen = screen
        self.running = True

        # Groups for sprites
        self.players = Group()
        self.enemies = Group()
        self.chars = Group()
        self.weapons = Group()
        self.projs_player = Group()
        self.projs_enemy = Group()
        self.all = LayeredDirty()

        # Room
        self.room = Room()
        self.all.add(self.room)

        # Players
        self.player = Player(self)
        self.players.add(self.player)
        self.all.add(self.players)

        # Enemies
        for enemy in range(0, randint(50,80)):
            enemy = NameMe(self)
            self.enemies.add(enemy)
        self.all.add(self.enemies)

        # Characters
        self.chars.add([self.players, self.enemies])

        # Projectiles
        self.projs = Group([self.projs_player, self.projs_enemy])

        # Layers
        self.all = LayeredDirty([
            self.room,
            self.enemies,
            self.players,
            self.projs ])

    def draw(self):
        """Draw all of the objects to the screen."""

        # Update all scene layers to the screen.
        self.all.update()
        self.dirty_rects = self.all.draw(self.screen)
        display.update(self.dirty_rects)
