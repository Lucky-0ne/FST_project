# Import and initialize the pygame library
import pygame

WN_HEIGHT = 600
WN_WIDTH = 800
inline_x = 8
gm_pause = True

clock = pygame.time.Clock()

# Set up the drawing window
pygame.init()
screen = pygame.display.set_mode((WN_WIDTH, WN_HEIGHT))