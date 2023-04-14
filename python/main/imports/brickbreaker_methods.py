# import dependencies and the random module (for random block position with each restart)
from imports.brickbreaker_objects import *

# method for calculating a random brick-position with varying brick sizes for each game start
def create_block_row(pos_y):
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
        life = random.randint(1, BLOCK_LIFE_MAX)
        clr = 255 - int(255 * life / BLOCK_LIFE_MAX)
        block_i = block(20, block_width, GAP + INLINE_X + sum(block_widths[:idx]) + (GAP * idx), pos_y, (0, clr, 0), life)
        blocks.append(block_i)
    
    return blocks

# generate the rows of bricks
def create_all_bricks(BRICK_ROWS=BRICK_ROWS):
    all_blocks = []
    for i in range(BRICK_ROWS):
        all_blocks += create_block_row(40 * (i + 1))

    return all_blocks

# block_pool
# all_blocks = create_all_bricks()

# check for collisions, remove objects and change projectile direction accordingly
def collision(all_blocks):

    projectile_hitbox = pygame.Rect(bullet.pos_x - bullet.radius, bullet.pos_y - bullet.radius, bullet.radius * 2, bullet.radius * 2)

    def brick_destruction_event():
        if block.life <= 1:
            block.life -= 1
            if np.abs(bullet.speed_x) < SPEED_CAP and (len(all_blocks) % 4) == 0:
                paddle.speed += PADDLE_SPEED * LVL_INCREMENT * (paddle.speed / np.abs(paddle.speed))
                bullet.speed_x += (BULLET_SPEED[0] * LVL_INCREMENT) * (bullet.speed_x / np.abs(bullet.speed_x))
                bullet.speed_y += BULLET_SPEED[1] * LVL_INCREMENT * (bullet.speed_y / np.abs(bullet.speed_y))
            all_blocks.remove(block)
        else:
            block.life -= 1
            block.colour = (0, 255 - int(255 * block.life / BLOCK_LIFE_MAX), 0)

    for block in all_blocks:
        block_rect = pygame.Rect(block.pos_x, block.pos_y, block.width, block.height)
        if block_rect.colliderect(projectile_hitbox) and ((bullet.pos_x < block.pos_x) or (bullet.pos_x > block.pos_x + block.width)):
            bullet.speed_x *= -1
            brick_destruction_event()
        elif block_rect.colliderect(projectile_hitbox):
            bullet.speed_y *= -1
            brick_destruction_event()

    paddle_rect = pygame.Rect(paddle.pos_x, paddle.pos_y, paddle.width, paddle.height)
    if paddle_rect.colliderect(projectile_hitbox) and ((bullet.pos_x < paddle.pos_x) or (bullet.pos_x > paddle.pos_x + paddle.width)):
        bullet.speed_x *= -1
    elif paddle_rect.colliderect(projectile_hitbox):
        bullet.speed_y *= -1

def hit(gm_pause):
    projectile_hitbox = pygame.Rect(bullet.pos_x - bullet.radius, bullet.pos_y - bullet.radius, bullet.radius * 2, bullet.radius * 2)
    wall_bottom_rect = pygame.Rect(wall_bottom.pos_x, wall_bottom.pos_y, wall_bottom.width, wall_bottom.height)
    if wall_bottom_rect.colliderect(projectile_hitbox):
        gm_pause = True

        return gm_pause
    
    return gm_pause