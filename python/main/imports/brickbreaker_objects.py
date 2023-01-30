from imports.brickbreaker_classes import *

projectile0 = projectile(400, 500, 5, (0, 0, 255), 3, 2)

paddle = block(10, 60, WN_WIDTH / 2 + 30, WN_HEIGHT - 25, (100, 0, 100))

wall_left = block(WN_HEIGHT - 10, 3, 5, 5, (0, 0, 0))
wall_right = block(WN_HEIGHT - 10, 3, WN_WIDTH - 8, 5, (0, 0, 0))
wall_top = block(3, WN_WIDTH - 10, 5, 5, (0, 0, 0))
wall_bottom = block(3, WN_WIDTH - 10, 5, WN_HEIGHT - 8, (255, 0, 0))

walls = [wall_left, wall_right, wall_top, wall_bottom]