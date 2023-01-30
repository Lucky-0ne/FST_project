# # Simple pygame program
from imports.brickbreaker_methods import *

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    for blockj in all_blocks:
        blockj.draws()

    for wall in walls:
        wall.draws()

    projectile0.draws()
    projectile0.bewegen()

    paddle.draws()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and paddle.posX < WN_WIDTH - 8 - 60:
        paddle.move(4)
    elif pressed[pygame.K_LEFT] and paddle.posX > 8:
        paddle.move(-4)

    if gm_pause:
        projectile0.posX = WN_WIDTH / 2
        projectile0.posY = 2 / 3 * WN_HEIGHT
        projectile0.speedX = 0
        projectile0.speedY = 0
        if pressed[pygame.K_SPACE]:
            projectile0.speedX = 3
            projectile0.speedY = 2
            gm_pause = False

    collision()

    clock.tick(60)

    # Flip the display
    pygame.display.flip()

pygame.quit()