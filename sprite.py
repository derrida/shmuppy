from pygame import Surface
from pygame.sprite import DirtySprite

class Sprite(DirtySprite):
    """The base sprite class that all sprites inherit."""

    def __init__(self, size, starting_hp, color=(0,0,0)):
        DirtySprite.__init__(self)
        self.image = Surface(size).convert()
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.hp = starting_hp

    def collide(self, scene):
        """Check if the sprite collided with an object or screen edge."""

        rect = self.rect.move([self.x, self.y])
        enemy_rects = []
        for enemy in scene.enemies:
            enemy_rects.append(enemy.rect)
        if rect.collidelistall(enemy_rects):
            return True

    def move(self):
        """Move the sprite and set it to dirty for the current frame."""

        self.dirty = 1
        self.rect.move_ip([self.x, self.y])
        self.rect.clamp_ip(self.scene.screen.get_rect())
