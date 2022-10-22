# Simple pygame program
# peggle-genre? --> Atari Breakout!

# Import and initialize the pygame library
import random
import pygame
pygame.init()

clock = pygame.time.Clock()

WN_HEIGHT = 600
WN_WIDTH = 800
inline_x = 8
gm_pause = True

# Set up the drawing window
screen = pygame.display.set_mode((WN_WIDTH, WN_HEIGHT))

class block:
    def __init__(self, height, width, posX, posY, colour):
        self.height = height
        self.width = width
        self.posX = posX
        self.posY = posY
        self.colour = colour
    
    def draws(self):
        pygame.draw.rect(screen, self.colour, ((self.posX, self.posY), (self.width, self.height)))

    def move(self, speed):
        self.posX += speed

class projectile:
    def __init__(self, posX, posY, radius, colour, speedX, speedY):
        self.posX = posX
        self.posY = posY
        self.radius = radius
        self.colour = colour
        self.speedX = speedX
        self.speedY = speedY

    def bewegen(self):
        if self.posX < 12:
            self.speedX *= -1
        elif self.posX > WN_WIDTH - 12:
            self.speedX *= -1
        self.posX = self.posX + self.speedX

        if self.posY < 12:
            self.speedY *= -1
        elif self.posY > WN_HEIGHT - 12:
            self.speedY *= -1
        self.posY = self.posY + self.speedY

    def draws(self):
        pygame.draw.circle(screen, self.colour, (self.posX, self.posY), self.radius, 0)

projectile0 = projectile(400, 500, 5, (0, 0, 255), 3, 2)
# projectile0 = projectile(400, 500, 5, (0, 0, 255), 0, 0)  # for debug only

paddle = block(10, 60, WN_WIDTH / 2 + 30, WN_HEIGHT - 25, (100, 0, 100))

wall_left = block(WN_HEIGHT - 10, 3, 5, 5, (0, 0, 0))
wall_right = block(WN_HEIGHT - 10, 3, WN_WIDTH - 8, 5, (0, 0, 0))
wall_top = block(3, WN_WIDTH - 10, 5, 5, (0, 0, 0))
wall_bottom = block(3, WN_WIDTH - 10, 5, WN_HEIGHT - 8, (255, 0, 0))
walls = [wall_left, wall_right, wall_top, wall_bottom]

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
        # blocki = block(20, block_width, gap + inline_x + (block_width + gap) * i, 300, (0, random.randint(0,255), 0))
        blocki = block(20, block_width, gap + inline_x + sum(block_widths[:i]) + (gap * i), posY, (0, random.randint(0,255), 0))
        blocks.append(blocki)
    
    return blocks

all_blocks = []
for i in range(5):
    all_blocks += create_blocks(40 * (i + 1))

# blocks.append(block(20, block_width, 700, 475, (0, 150, 0)))  # for debug only

def collision():
    global all_blocks, gm_pause

    project_rect = pygame.Rect(projectile0.posX - projectile0.radius, projectile0.posY - projectile0.radius, projectile0.radius * 2, projectile0.radius * 2)

    wall_bottom_rect = pygame.Rect(wall_bottom.posX, wall_bottom.posY, wall_bottom.width, wall_bottom.height)
    if wall_bottom_rect.colliderect(project_rect):
        gm_pause = True

    # pygame.draw.rect(screen, ('yellow'), project_rect, 2)   # hitbox
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
    # block1.draws()

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