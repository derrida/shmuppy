import os
import random
import pygame
from constants import *
from room import Room
from player import Player
from enemy import Enemy

class Game(object):
    """The main game object."""

    def __init__(self):
        self.running = True
        self.create_game()
        self.create_sprites()
        self.play()

    def create_game(self):
        """Creates the game window and clock."""

        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.screen = pygame.display.set_mode(RESOLUTION, False, 32)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("%s %s" % (GAME_NAME, GAME_VER))
        pygame.mouse.set_visible(False)
        if FULL_SCREEN:
            pygame.display.toggle_fullscreen()

    def create_sprites(self):
        """Create all the required sprites and add them to groups."""

        # Game objects
        self.room = Room()
        self.player = Player()
        self.enemy = Enemy()
        self.projectiles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        # Create a random amount of enemies
        for enemy in range(0, random.randint(0,20)):
            enemy = Enemy()
            self.enemies.add([enemy])

        # Rendered layers
        self.all = pygame.sprite.LayeredDirty([
            self.room,
            self.player,
            self.enemies,
            self.projectiles ])

        # Pass the game object to all sprites so they know about other sprites
        for sprite in self.all:
            sprite.game = self

    def play(self):
        """The main game loop."""

        while self.running:
            self.clock.tick(FPS)
            self.check_events()
            self.draw_screen()
            self.show_debug()

    def check_events(self):
        """Check for user input."""

        for event in pygame.event.get():

            # Check for window destroy event
            if event.type == QUIT:
                self.running = False

            # Pressed keys
            elif event.type == KEYDOWN:

                # Quits the game
                if event.key == QUIT:
                    self.running = False

                # Player movement
                elif event.key == UP:
                    self.player.y -= MOVE_OFFSET
                elif event.key == DOWN:
                    self.player.y += MOVE_OFFSET
                elif event.key == LEFT:
                    self.player.x -= MOVE_OFFSET
                elif event.key == RIGHT:
                    self.player.x += MOVE_OFFSET

                # Player shoot weapon
                if event.key == FIRE:
                    self.player.shoot()

            # Released keys
            elif event.type == KEYUP:

                # Stop player movement
                if event.key in (UP, DOWN):
                    self.player.y = 0
                elif event.key in (LEFT, RIGHT):
                    self.player.x = 0

    def draw_screen(self):
        """Draw all of the objects to the screen."""

        self.all.update()
        self.dirty_rects = self.all.draw(self.screen)
        pygame.display.update(self.dirty_rects)

    def show_debug(self):
        """Print debug info to console output."""

        if SHOW_DEBUG:

            # Show dirty screen areas in console output.
            for i in range(0, len(self.dirty_rects)):
                print "Dirty screen areas: %sx%s @ %s,%s" % (
                    self.dirty_rects[i][2], self.dirty_rects[i][3],
                    self.dirty_rects[i][0], self.dirty_rects[i][1])

            # Show current framerate on screen.
            print 'Framerate: %f/%f' % (self.clock.get_fps(), FPS)
