import pygame
from sprite import *

class Game(object):
    """The main game object."""

    def __init__(self):
        self.running = True
        self.create_game()
        self.create_sprites()
        self.play()

    def create_game(self):
        """Creates the game window and clock."""

        self.screen = pygame.display.set_mode(RESOLUTION, False, 32)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("%s %s" % (GAME_NAME, GAME_VER))
        pygame.mouse.set_visible(False)
        if FULL_SCREEN:
            pygame.display.toggle_fullscreen()

    def create_sprites(self):
        """Create all the required sprites and add them to their appropriate
        sprite groups."""

        self.room = Room()
        self.player = Player()
        self.enemy = Enemy()

        self.all = pygame.sprite.LayeredDirty([
            self.room,
            self.player,
            self.enemy ])

    def play(self):
        """The main game loop that limits the speed, checks for events, and
            then draws the changed areas of the screen."""

        while self.running:
            self.clock.tick(FPS)
            self.check_events()
            self.draw_screen()

    def check_events(self):
        """Check for user input."""

        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                elif event.key in PLAYER_MOVE_KEYS:
                    self.player.move(True, event.key)
            elif event.type == KEYUP:
                if event.key in PLAYER_MOVE_KEYS:
                    self.player.move(False, event.key)

    def draw_screen(self):
        """Draw all of the objects to the screen."""

        self.all.update()
        dirty_rects = self.all.draw(self.screen)
        pygame.display.update(dirty_rects)
