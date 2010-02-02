from math import degrees, atan2
from pygame import transform
from sprite import Sprite

class Projectile(Sprite):
    """The base that other projectiles inherit."""

    def __init__(self, scene, size, color, power, speed, range):
        Sprite.__init__(self, scene, size, color)
        self.power = power
        self.speed = speed
        self.range = range
        self.add()

    def add(self):
        """Add the projectile to the scene for rendering."""

        self.scene.projs.add(self)
        self.scene.all.add(self.scene.projs)
        self.rotate()

    def rotate(self):
        """Rotate the projectile to the direction it was fired in."""

        self.x, self.y = self.scene.player.facing
        rotation = degrees(atan2(self.x, self.y))
        self.image = transform.rotate(self.image, rotation)
        self.rect = self.image.get_rect(left=self.rect.left, top=self.rect.top)
        self.rect.centerx = self.scene.player.rect.centerx + (8 * self.x)
        self.rect.centery = self.scene.player.rect.centery + (8 * self.y)

    def move(self):
        """Draw the projectile's new position."""

        if self.range > 0:
            self.dirty = 1
            self.rect.move_ip([self.x * self.speed, self.y * self.speed])
            self.range -= self.speed
        else:
            self.kill()

    def collide(self):
        """Check if the projectile collides with something."""

        # Kill projectile when it hits a screen edge
        if not self.rect.colliderect(self.scene.screen.get_rect()):
            self.kill()

        # Kill projectile when it hits a character, and also damage character.
        for char in self.scene.chars:
            if self.rect.colliderect(char.rect):
                char.damage(self.power)
                self.damage()

    def damage(self):
        """TODO: Fix this description:     The projectile is damaged."""

        self.kill()


class Arrow(Projectile):
    """An Arrow is a single projectile."""

    def __init__(self, scene):
        size = (1,20)
        color = (127,128,255)
        speed = 6
        power = 600
        range = 100
        Projectile.__init__(self, scene, size, color, power, speed, range)


class Laser(Projectile):
    """A Bullet is a single projectile."""

    def __init__(self, scene):
        size = (2,10)
        color = (255,0,128)
        speed = 3
        power = 0.2
        range = 50
        Projectile.__init__(self, scene, size, color, power, speed, range)

class Particle(Projectile):
    """A Particle is a single projectile."""

    def __init__(self, scene):
        size = (3,3)
        color = (207,0,255)
        speed = 15
        power = 6
        range = 200
        Projectile.__init__(self, scene, size, color, power, speed, range)

