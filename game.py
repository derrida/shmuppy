import os
from pygame import display, time, mouse
from input import EventManager
from scene import Scene
from config import *

class Game(object):
    """The main game object."""

    def __init__(self):
        self.framecount = 0
        self.create_game()
        self.play()

    def create_game(self):
        """Initializes the game."""

        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.screen = display.set_mode(RESOLUTION, False, 32)
        self.scene = Scene(self.screen)
        self.events = EventManager(self.scene)
        self.clock = time.Clock()
        display.set_caption("%s %s" % (NAME, VERSION))
        mouse.set_visible(False)
        if FULLSCREEN:
            toggle_fullscreen()

    def play(self):
        """The main game loop."""

        while self.scene.running:
            self.clock.tick(FPS)
            self.events.check()
            self.scene.draw()
            self.show_debug()

    def show_debug(self):
        """Print debug info to console output."""

        if DEBUG:
            if self.framecount == FPS:

                # Show dirty screen areas in console output.
                rects = self.scene.dirty_rects
                dirty = "dirty: 0, "
                for rect in rects:
                    dirty = "dirty: %d, " % len(rects)

                # Print number of projectiles on the screen
                projs = "projs: %s, " % len(self.scene.projs)

                # Show current framerate on screen.
                fps = "fps: %d/%d" % (self.clock.get_fps(), FPS)
                self.framecount = 0
                os.system("clear")
                print "Game: " + dirty, projs, fps

            else:
                self.framecount += 1
