import math
import pygame
from pygame.locals import *

def draw_circle (surface, color, offset, radius, scale=4):
    rect_size = radius*2*scale
    rect_size_half = radius*scale
    temp = pygame.Surface((rect_size,rect_size), SRCALPHA)
    temp.fill((color[0], color[1], color[2], 0))
    pygame.draw.circle(temp,color, (rect_size_half, rect_size_half),
        rect_size_half)
    surface.blit(pygame.transform.smoothscale(temp, (radius*2,radius*2)),
        (offset[0]-radius, offset[1]-radius))
