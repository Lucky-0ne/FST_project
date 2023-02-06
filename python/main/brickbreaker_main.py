# # simple pygame program
# first import dependencies
from imports.brickbreaker_methods import *
import time

# run until the user asks to quit or the time runs up
running = True
time_start = time.time()
while running and (time.time() - time_start) < TIME_LIMIT:
    # check if the user clicked the window close button --> end while/program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # white background
    screen.fill((255, 255, 255))

    # draw bricks, walls, the projectile and paddle
    for block_i in all_blocks:
        block_i.draws()

    for wall in walls:
        wall.draws()

    bullet.draws()
    bullet.bewegen()

    paddle.draws()

    # check user input and move paddle
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and paddle.pos_x < WN_WIDTH - INLINE_X - PADDLE_WIDTH:
        paddle.move(4)
    elif pressed[pygame.K_LEFT] and paddle.pos_x > INLINE_X:
        paddle.move(-4)

    # check if game is paused, position the projectile and start game if space-key is pressed
    if gm_pause:
        bullet.pos_x = WN_WIDTH / 2
        bullet.pos_y = 2 / 3 * WN_HEIGHT
        bullet.speed_x = 0
        bullet.speed_y = 0
        if pressed[pygame.K_SPACE]:
            bullet.speed_x = 3
            bullet.speed_y = 2
            gm_pause = False

    # check collisions
    collision()

    # set tick rate
    clock.tick(60)

    # flip the display
    pygame.display.flip()

pygame.quit()