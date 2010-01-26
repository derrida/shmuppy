import os
import pygame
from constants import *
from room import Room
from player import Player
from enemy import Enemy
from projectiles import *

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

        # Projectiles
        self.projectiles = pygame.sprite.Group()

        # Rendered layers
        self.all = pygame.sprite.LayeredDirty([
            self.room,
            self.player,
            self.enemy,
            self.projectiles ])

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
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                elif event.key == UP:
                    self.player.y -= MOVE_OFFSET
                elif event.key == DOWN:
                    self.player.y += MOVE_OFFSET
                elif event.key == LEFT:
                    self.player.x -= MOVE_OFFSET
                elif event.key == RIGHT:
                    self.player.x += MOVE_OFFSET
                elif event.key == K_z:
                    self.player.shoot()
            elif event.type == KEYUP:
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
