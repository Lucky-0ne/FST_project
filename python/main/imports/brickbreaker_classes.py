from imports.brickbreaker_init import *

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