import pygame
import sys
import random

fruitBlossom = pygame.image.load('fruitblossom.png')

class Fruit(pygame.sprite.Sprite):
# build the contructor
    def __init__(self, width, height):
        super().__init__()
        # create the sprite and fill with color (update with images)
        self.image = fruitBlossom
        #self.image.fill(color)
        
        self.width = width
        self.height = height
        # set start position of fruit with random
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(100, 700)
        self.rect.y = random.randrange(135, 350)
