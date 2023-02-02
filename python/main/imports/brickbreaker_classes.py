# import dependencies
from imports.brickbreaker_init import *

# class for blocks (used for the bricks in game)
class block:
    def __init__(self, height, width, pos_x, pos_y, colour):
        self.height = height
        self.width = width
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.colour = colour
    
    def draws(self):
        pygame.draw.rect(screen, self.colour, ((self.pos_x, self.pos_y), (self.width, self.height)))

    def move(self, speed):
        self.pos_x += speed

# class for projectiles (currently just one)
class projectile:
    def __init__(self, pos_x, pos_y, radius, colour, speed_x, speed_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = radius
        self.colour = colour
        self.speed_x = speed_x
        self.speed_y = speed_y

    def bewegen(self):
        if self.pos_x < 12:
            self.speed_x *= -1
        elif self.pos_x > WN_WIDTH - 12:
            self.speed_x *= -1
        self.pos_x = self.pos_x + self.speed_x

        if self.pos_y < 12:
            self.speed_y *= -1
        elif self.pos_y > WN_HEIGHT - 12:
            self.speed_y *= -1
        self.pos_y = self.pos_y + self.speed_y

    def draws(self):
        pygame.draw.circle(screen, self.colour, (self.pos_x, self.pos_y), self.radius, 0)