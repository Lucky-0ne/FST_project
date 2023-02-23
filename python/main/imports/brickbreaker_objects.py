# first import dependencies
from imports.brickbreaker_classes import *

# create game objects
bullet = projectile(400, 500, 5, (0, 0, 255), BULLET_SPEED[0], BULLET_SPEED[1])

paddle = paddles(10, PADDLE_WIDTH, WN_WIDTH / 2 + 30, WN_HEIGHT - 25, (100, 0, 100), PADDLE_SPEED)

wall_left = block(WN_HEIGHT - 10, 3, 5, 5, (0, 0, 0))
wall_right = block(WN_HEIGHT - 10, 3, WN_WIDTH - INLINE_X, 5, (0, 0, 0))
wall_top = block(3, WN_WIDTH - 10, 5, 5, (0, 0, 0))
wall_bottom = block(3, WN_WIDTH - 10, 5, WN_HEIGHT - INLINE_X, (255, 0, 0))

walls = [wall_left, wall_right, wall_top, wall_bottom]