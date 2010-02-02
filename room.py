from pygame import draw
from sprite import Sprite
import config

class Room(Sprite):
    """A room is an area where a fight to the death takes place."""

    def __init__(self, scene):
        color = (0,0,0)
        room_size = config.RESOLUTION
        self.tile = FloorTile(scene)
        self.num_tiles = [
            config.RESOLUTION[0] / self.tile.size[0],
            config.RESOLUTION[1] / self.tile.size[1] ]
        Sprite.__init__(self, scene, room_size, color)
        self.make_floor()

    def make_floor(self):
        """Create the room of floor tiles."""

        for y in range(0, self.num_tiles[1] + 1):
            for x in range(0, self.num_tiles[0] + 1):
                offset = (x * self.tile.size[0], y * self.tile.size[1])
                self.image.blit(self.tile.image, offset)


class FloorTile(Sprite):
    """A room is made up of many floor tiles."""

    def __init__(self, scene):
        color = (43,73,85)
        grid_color = (170,170,170)
        self.size = (16,16)
        Sprite.__init__(self, scene, self.size, color)
        if config.DEBUG:
            offset = self.rect.move([1,1])
            draw.rect(self.image, grid_color, offset, 1)
