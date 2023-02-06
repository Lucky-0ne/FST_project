# Import and initialize the pygame library
import os
import pygame
pygame.init()
os.environ["SDL_VIDEODRIVER"] = "dummy"

# initialize constants
WN_HEIGHT = 600
WN_WIDTH = 800
INLINE_X = 8
PADDLE_WIDTH = 60
BRICK_ROWS = 7

# initialize variables
gm_pause = True
clock = pygame.time.Clock()

# set up the drawing window
screen = pygame.display.set_mode((WN_WIDTH, WN_HEIGHT))