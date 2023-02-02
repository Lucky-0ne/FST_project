# import dependencies and the random module (for random block position with each restart)
from imports.brickbreaker_objects import *
import random

# method for calculating a random brick-position with varying brick sizes for each game start
def create_blocks(pos_y):
    '''
    Calculates a random brick-position with varying brick sizes for each game start.

    input:
        pos_y [int] --> vertical starting position of the brick row
        
    output:
        blocks [list of objects] --> list contains each generated brick-object (block)
    '''

    GAP = 10
    MAX_WIDTH = 90
    RANGE_X = WN_WIDTH - 200
    block_widths=[]
    while RANGE_X > (MAX_WIDTH + 2 * GAP):
        a1 = random.randrange(30, MAX_WIDTH, 10)
        RANGE_X -= a1
        block_widths.append(a1)
    block_widths += [RANGE_X]
    block_widths += [WN_WIDTH - (2 * INLINE_X) - sum(block_widths) - ((len(block_widths) + 2) * GAP)]

    blocks = []
    for idx, block_width in enumerate(block_widths):
        block_i = block(20, block_width, GAP + INLINE_X + sum(block_widths[:idx]) + (GAP * idx), pos_y, (0, random.randint(0,255), 0))
        blocks.append(block_i)
    
    return blocks

# generate the rows of bricks
all_blocks = []
for i in range(BRICK_ROWS):
    all_blocks += create_blocks(40 * (i + 1))

# check for collisions, remove objects and change projectile direction accordingly
def collision():
    global all_blocks, gm_pause

    project_rect = pygame.Rect(bullet.pos_x - bullet.radius, bullet.pos_y - bullet.radius, bullet.radius * 2, bullet.radius * 2)

    wall_bottom_rect = pygame.Rect(wall_bottom.pos_x, wall_bottom.pos_y, wall_bottom.width, wall_bottom.height)
    if wall_bottom_rect.colliderect(project_rect):
        gm_pause = True

    for block in all_blocks:
        block_rect = pygame.Rect(block.pos_x, block.pos_y, block.width, block.height)
        if block_rect.colliderect(project_rect) and ((bullet.pos_x < block.pos_x) or (bullet.pos_x > block.pos_x + block.width)):
            bullet.speed_x *= -1
            all_blocks.remove(block)
        elif block_rect.colliderect(project_rect):
            bullet.speed_y *= -1
            all_blocks.remove(block)

    paddle_rect = pygame.Rect(paddle.pos_x, paddle.pos_y, paddle.width, paddle.height)
    if paddle_rect.colliderect(project_rect) and ((bullet.pos_x < paddle.pos_x) or (bullet.pos_x > paddle.pos_x + paddle.width)):
        bullet.speed_x *= -1
    elif paddle_rect.colliderect(project_rect):
        bullet.speed_y *= -1