from sprite import Sprite

class Projectile(Sprite):
    """The base that other projectiles inherit."""

    def __init__(self, scene, size, color, speed):
        Sprite.__init__(self, size, color)
        self.scene = scene
        self.speed = speed + self.scene.player.speed

    def move(self):
        """Draw the projectile's new position."""

        self.dirty = 1
        self.rect.move_ip([self.x * self.speed, self.y * self.speed])

    def update(self):
        """Update the projectile on the screen."""

        # Remove all projectiles that go off of the screen.
        for proj in self.scene.projs:
            if not proj.rect.colliderect(self.scene.screen.get_rect()):
                proj.kill()

        # Damage enemy when player's projectile hits it
        for proj in self.scene.projs_enemy:
            for char in self.scene.players:
                if proj.rect.colliderect(char.rect):
                    proj.kill()
                    char.damage()

        # Damage player when enemy's projectile hits it
        for proj in self.scene.projs_player:
            for char in self.scene.enemies:
                if proj.rect.colliderect(char.rect):
                    proj.kill()
                    char.damage()

        # Move projectile
        if (self.x or self.y):
            self.move()


class Bullet(Projectile):
    """A Bullet is a single projectile."""

    def __init__(self, scene):
        size = (10, 20)
        color = (255,0,128)
        speed = 6
        Projectile.__init__(self, scene, size, color, speed)


class Arrow(Projectile):
    """A Arrow is a single projectile."""

    def __init__(self, scene):
        size = (1,8)
        color = (127,128,0)
        speed = 14
        Projectile.__init__(self, scene, size, color, speed)


class Grenade(Projectile):
    """A Grenade is a single projectile."""

    def __init__(self, scene):
        size = (4,6)
        color = (255,120,50)
        speed = 1
        Projectile.__init__(self, scene, size, color, speed)


class Particle(Projectile):
    """A Particle is a single projectile."""

    def __init__(self, scene):
        size = (1,1)
        color = (255,255,255)
        speed = 2
        Projectile.__init__(self, scene, size, color, speed)
