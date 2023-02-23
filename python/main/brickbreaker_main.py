# # simple pygame program
# first import dependencies
from imports.brickbreaker_methods import *
import time


# run until the user asks to quit or the time runs up
running = True
while running:
    # check if the user clicked the window close button --> end while/program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # white background
    screen.fill((255, 255, 255))

    # draw bricks, walls, the projectile and paddle
    for block_i in all_blocks:
        block_i.draws()
        
        text_surface = TEXT_FONT.render(f"{block_i.life}", False, (255, 255, 255))
        screen.blit(text_surface, (block_i.pos_x + (block_i.width / 2), block_i.pos_y))

    for wall in walls:
        wall.draws()

    bullet.draws()
    bullet.bewegen()

    paddle.draws()

    # check user input and move paddle
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and paddle.pos_x < WN_WIDTH - INLINE_X - PADDLE_WIDTH:
        paddle.move(paddle.speed)
    elif pressed[pygame.K_LEFT] and paddle.pos_x > INLINE_X:
        paddle.move(-1 * paddle.speed)

    gm_pause = hit(gm_pause)

    # check if game is paused, position the projectile and start game if space-key is pressed
    if gm_pause:
        bullet.pos_x = WN_WIDTH / 2
        bullet.pos_y = 2 / 3 * WN_HEIGHT
        bullet.speed_x = 0
        bullet.speed_y = 0
        if pressed[pygame.K_SPACE]:
            bullet.speed_x = BULLET_SPEED[0] * [-1,1][random.randint(0,1)]
            bullet.speed_y = BULLET_SPEED[1]
            paddle.speed = PADDLE_SPEED
            gm_pause = False

    # check collisions
    collision()

    # set tick rate
    clock.tick(60)

    # flip the display
    pygame.display.flip()

pygame.quit()