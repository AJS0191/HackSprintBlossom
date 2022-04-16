# import pygame package
import pygame
import sys
import random

# initializing imported module
pygame.init()

# displaying a window of height
display_surface = pygame.display.set_mode((850, 600))
# screen = pygame.display.set_mode((850, 600))
# Making background image
# image = pygame.image.load('tree.png')
carrot = pygame.image.load('carrot.png')

# color constants 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
# building the fruit class
class Fruit(pygame.sprite.Sprite):
# build the contructor
    def __init__(self, width, height, color):
        super().__init__()
        # create the sprite and fill with color (update with images)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # set start position of fruit with random
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(30, 820)
        self.rect.y = random.randrange(30, 300)


# create a list to hold the fruit sprites
fruitList = pygame.sprite.Group()
# create a list that holds all sprites
spriteList = pygame.sprite.Group()

# create the fruits
numberFruits = 10
for i in range(0, numberFruits):
    blawesomeFruit = Fruit(10, 10, GREEN)
    fruitList.add(blawesomeFruit)
    spriteList.add(blawesomeFruit)
fruit_y = 10
fruit_x = 10
#displaying tree to background
#screen.fill(color)
clock = pygame.time.Clock()

# creating a bool value which checks
# if game is running
running = True

# keep game running till running is true
while running:

    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():

        # if event is of type quit then
        # set running bool to false
        if event.type == pygame.QUIT:
            running = False

    # fill the background of the game
    display_surface.fill ((0, 0, 0))

    # draw to the screen

    spriteList.draw(display_surface)
    # pygame.draw.rect(display_surface, color, (fruit_x, fruit_y, 20, 20))
    # pygame.draw.rect(display_surface, color, (fruit_x + 70, fruit_y + 10, 20, 20))
    # pygame.draw.rect(display_surface, color, (fruit_x + 180, fruit_y + 18, 20, 20))
    # display_surface.blit(image,(0,0))
    # display_surface.blit(carrot, (10,10))
    # fruit_y = fruit_y + 5

    # update display
    pygame.display.flip()
    clock.tick(60)
