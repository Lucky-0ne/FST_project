from imports.brickbreaker_objects import *
import random

def create_blocks(posY):
    gap = 10
    max_width = 90
    block_widths=[]
    range_x = WN_WIDTH - 200
    while range_x > (max_width + 2 * gap):
        a1 = random.randrange(30, max_width, 10)
        range_x -= a1
        block_widths.append(a1)
    block_widths += [range_x]
    block_widths += [WN_WIDTH - (2 * inline_x) - sum(block_widths) - ((len(block_widths) + 2) * gap)]

    blocks = []
    for i, block_width in enumerate(block_widths):
        blocki = block(20, block_width, gap + inline_x + sum(block_widths[:i]) + (gap * i), posY, (0, random.randint(0,255), 0))
        blocks.append(blocki)
    
    return blocks

all_blocks = []
for i in range(5):
    all_blocks += create_blocks(40 * (i + 1))

def collision():
    global all_blocks, gm_pause

    project_rect = pygame.Rect(projectile0.posX - projectile0.radius, projectile0.posY - projectile0.radius, projectile0.radius * 2, projectile0.radius * 2)

    wall_bottom_rect = pygame.Rect(wall_bottom.posX, wall_bottom.posY, wall_bottom.width, wall_bottom.height)
    if wall_bottom_rect.colliderect(project_rect):
        gm_pause = True

    for block in all_blocks:
        block_rect = pygame.Rect(block.posX, block.posY, block.width, block.height)
        if block_rect.colliderect(project_rect) and ((projectile0.posX < block.posX) or (projectile0.posX > block.posX + block.width)):
            projectile0.speedX *= -1
            all_blocks.remove(block)
        elif block_rect.colliderect(project_rect):
            projectile0.speedY *= -1
            all_blocks.remove(block)

    paddle_rect = pygame.Rect(paddle.posX, paddle.posY, paddle.width, paddle.height)
    if paddle_rect.colliderect(project_rect) and ((projectile0.posX < paddle.posX) or (projectile0.posX > paddle.posX + paddle.width)):
        projectile0.speedX *= -1
    elif paddle_rect.colliderect(project_rect):
        projectile0.speedY *= -1