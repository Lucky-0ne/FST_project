# Import and initialize the pygame library
import os
import random
import numpy as np
import pygame
pygame.init()
pygame.font.init()
os.environ["SDL_VIDEODRIVER"] = "dummy"

# initialize constants
WN_HEIGHT = 600
WN_WIDTH = 800
INLINE_X = 8
PADDLE_WIDTH = 60
BRICK_ROWS = 7
BULLET_SPEED = (3, 2)
PADDLE_SPEED = 4
SPEED_CAP = 5
TEXT_FONT = pygame.font.SysFont("Comic Sans MS", 15)

# initialize variables
gm_pause = True
clock = pygame.time.Clock()

# set up the drawing window
screen = pygame.display.set_mode((WN_WIDTH, WN_HEIGHT))