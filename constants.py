from pygame.locals import *

GAME_NAME = "Shmuppy"
GAME_VER = ""

# Options
RESOLUTION = (600,800)
FULL_SCREEN = False
FPS = 60

# Debugging
SHOW_DEBUG = False
PROFILE = False

# Controls
QUIT = K_ESCAPE
UP = K_UP
DOWN = K_DOWN
LEFT = K_LEFT
RIGHT = K_RIGHT
FIRE = K_LCTRL
MOVE_OFFSET = 3

# Player
PLAYER_COLOR = (100,0,0)
PLAYER_SIZE = (24,24)

# Ememies
ENEMY_COLOR = (0,100,0)
ENEMY_SIZE = (24,24)

# Room
ROOM_COLOR = (43,73,85)
GRID_COLOR = (170,170,170)
SCREEN_RECT = Rect(0, 0, RESOLUTION[0], RESOLUTION[1])
TILE_SIZE = (32,32)
ROOM_TILES = [ RESOLUTION[0] / TILE_SIZE[0], RESOLUTION[1] / TILE_SIZE[1] ]

# Projectiles
ARROW_COLOR = (255,255,255)
ARROW_SIZE = (1,8)
