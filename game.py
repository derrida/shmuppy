import os
from pygame import display, time, mouse
from input import EventManager
from scene import Scene
from config import *

class Game(object):
    """The main game object."""

    def __init__(self):
        self.framecount = 0
        self.repeat_keys = {}
        self.create_game()
        self.play()

    def create_game(self):
        """Initializes the game."""

        # COnfigure the game
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
                dirty = ""
                for i in range(0, len(self.dirty_rects)):
                    dirty = "dirty: %sx%s @ %s,%s, " % (self.dirty_rects[i][2],
                        self.dirty_rects[i][3], self.dirty_rects[i][0],
                        self.dirty_rects[i][1])

                # Print number of projectiles on the screen
                projs = "projs: %s, " % len(self.scene.projs)

                # Show current framerate on screen.
                fps = "fps: %d/%d" % (self.clock.get_fps(), FPS)
                self.framecount = 0
                print dirty, projs, fps

            else:
                self.framecount += 1
