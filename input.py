from pygame import event, time
from pygame.locals import *
from config import *

class EventManager(object):
    """Responds to user input and custom-made events as they are triggered."""

    def __init__(self, scene):

        self.scene = scene

    def check(self):
        """Check for user input."""

        event_rapidfire = USEREVENT + 1

        for e in event.get():

            # Check for window destroy event
            if e.type == QUIT:
                self.scene.running = False

            # Pressed keys
            elif e.type == KEYDOWN:

                # Quits the game
                if e.key == QUIT:
                    self.scene.running = False

                # Move player
                elif e.key == UP:
                    self.scene.player.y -= self.scene.player.speed
                elif e.key == DOWN:
                    self.scene.player.y += self.scene.player.speed
                elif e.key == LEFT:
                    self.scene.player.x -= self.scene.player.speed
                elif e.key == RIGHT:
                    self.scene.player.x += self.scene.player.speed

                # Player shoot weapon
                elif e.key == FIRE:
                    self.scene.player.shoot()
                    time.set_timer(event_rapidfire, 120)

            # Released keys
            elif e.type == KEYUP:

                # Stop player
                if e.key in (UP, DOWN):
                    self.scene.player.y = 0
                elif e.key in (LEFT, RIGHT):
                    self.scene.player.x = 0

                # Stop repeating key when released
                elif e.key == FIRE:
                    time.set_timer(event_rapidfire, 0)

            # Custom event - Rapid fire
            if e.type == event_rapidfire:
                self.scene.player.shoot()
