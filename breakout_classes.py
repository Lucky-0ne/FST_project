import pygame

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