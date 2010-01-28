import os
from random import randint
from pygame import display, time, mouse, event
from pygame.sprite import Group, LayeredDirty
from pygame.locals import *
from room import Room
from player import Player
from enemy import Enemy
from config import *

class Game(object):
    """The main game object."""

    def __init__(self):
        self.running = True
        self.framecount = 0
        self.repeat_keys = {}
        self.create_game()
        self.create_sprites()
        self.play()

    def create_game(self):
        """Initializes the game."""

        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.screen = display.set_mode(RESOLUTION, False, 32)
        self.clock = time.Clock()
        display.set_caption("%s %s" % (NAME, VERSION))
        mouse.set_visible(False)
        if FULLSCREEN:
            toggle_fullscreen()

    def create_sprites(self):
        """Create all the required sprites and add them to groups."""

        # Groups for sprites
        self.weapons = Group()
        self.projectiles = Group()
        self.enemies = Group()

        # Game Sprites
        self.room = Room()
        self.player = Player(self)
        for enemy in range(0, randint(20,70)):
            enemy = Enemy(self)
            self.enemies.add(enemy)

        # Rendered layers
        self.all = LayeredDirty([
            self.room,
            self.player,
            self.enemies,
            self.projectiles ])

    def play(self):
        """The main game loop."""

        while self.running:
            self.clock.tick(FPS)
            self.check_events()
            self.draw_screen()
            self.show_debug()

    def check_events(self):
        """Check for user input."""

        event_rapidfire = USEREVENT + 1

        for e in event.get():

            # Check for window destroy event
            if e.type == QUIT:
                self.running = False

            # Pressed keys
            elif e.type == KEYDOWN:

                # Quits the game
                if e.key == QUIT:
                    self.running = False

                # Move player
                elif e.key == UP:
                    self.player.y -= self.player.speed
                elif e.key == DOWN:
                    self.player.y += self.player.speed
                elif e.key == LEFT:
                    self.player.x -= self.player.speed
                elif e.key == RIGHT:
                    self.player.x += self.player.speed

                # Player shoot weapon
                elif e.key == FIRE:
                    time.set_timer(event_rapidfire, 120)

            # Released keys
            elif e.type == KEYUP:

                # Stop player
                if e.key in (UP, DOWN):
                    self.player.y = 0
                elif e.key in (LEFT, RIGHT):
                    self.player.x = 0

                # Stop repeating key when released
                elif e.key == FIRE:
                    time.set_timer(event_rapidfire, 0)

            # Custom event - Rapid fire
            elif e.type == event_rapidfire:
                self.player.shoot()


    def draw_screen(self):
        """Draw all of the objects to the screen."""

        # Remove projectiles when the go off of the screen.
        for proj in self.projectiles:
            if not proj.rect.colliderect(self.screen.get_rect()):
                proj.kill()

        # Update all layers of the screen.
        self.all.update()
        self.dirty_rects = self.all.draw(self.screen)
        display.update(self.dirty_rects)

    def show_debug(self):
        """Print debug info to console output."""

        if DEBUG:
            if self.framecount == FPS:

                # Show dirty screen areas in console output.
                dirty = ""
                for i in range(0, len(self.dirty_rects)):
                    dirty = "dirty: %sx%s @ %s,%s, " % (self.dirty_rects[i][2],
                        self.dirty_rects[i][3], self.dirty_rects[i][0],
                        self.dirty_rects[i][1])

                # Print number of projectiles on the screen
                projs = "projs: %s, " % len(self.projectiles)

                # Show current framerate on screen.
                fps = "fps: %d/%d" % (self.clock.get_fps(), FPS)
                self.framecount = 0
                print dirty, projs, fps

            else:
                self.framecount += 1
