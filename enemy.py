from random import randint
from character import Character

class Enemy(Character):
    """An enemy sprite."""

    def __init__(self, scene, size, color, name, speed, hp):
        Character.__init__(self, scene, size, color, name, speed, hp)
        self.rect.move_ip([ size[0] * randint(0, self.scene.room.num_tiles[0]),
            size[1] * randint(0, self.scene.room.num_tiles[1]) ])

    def take_damage(self):
        """TODO: Damage should be inflicted upong an enemy which results in a
        call to this function. This function will assess damage to the mob
        based on certain fixed and dynamic criteria."""


class Human(Enemy):
    """This is the human class. They come in a variety of sub-classes. Each
        human carries up to 2 weapons and up to 3 grenades. This depends upon
        the sub-class"""

    def __init__(self, scene):
        name = "Human"
        size = (16,16)
        color = (122,43,92)
        speed = 2
        hp = 5
        Enemy.__init__(self, scene, size, color, name, speed, hp)


class Glork(Enemy):
    """Some orc-like thing. They're dumb, not very smart, and easy to kill.
        They come in a variety of sub-classes."""

    def __init__(self, scene):
        name = "Glork"
        size = (16,16)
        color = (30,243,192)
        speed = 2
        hp = 10
        Enemy.__init__(self, scene, size, color, name, speed, hp)


