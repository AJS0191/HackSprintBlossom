# import pygame package
from turtle import speed
import pygame
import sys
import random

# initializing imported module
pygame.init()

# displaying a window of height
display_surface = pygame.display.set_mode((850, 600))

# set the clock
clock = pygame.time.Clock()
currentTime = 0
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
    def __init__(self, width, height, color, speed):
        super().__init__()
        # create the sprite and fill with color (update with images)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.color = color
        self.width = width
        self.height = height
        # set start position of fruit with random
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(30, 820)
        self.rect.y = random.randrange(30, 300)
        self.speed = speed

    # def update(self):
        # self.rect.y = self.rect.y + self.speed


# adding the blossom class for falling objects from fruit ((i think i named this backwards))
class Blossom(pygame.sprite.Sprite):
    def __init__(self, fruit):
        super().__init__()
        self.color = WHITE  # change to fruit.color
        self.width = fruit.width
        self.height = fruit.height
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(fruit.color)
        self.speed = random.randrange(1, 3)
        self.updateTime = random.randrange(0, 30000)
        self.rect = self.image.get_rect()
        self.rect.x = fruit.rect.x
        self.rect.y = fruit.rect.y

    def update(self):
        # only drops fruit at random intervals
        if currentTime > self.updateTime:
            self.image = pygame.Surface([20, 20])
            pygame.transform.scale(carrot, (20, 20), dest_surface=self.image)
            self.rect.y = self.rect.y + self.speed


# create a list to hold the fruit sprites
fruitList = pygame.sprite.Group()
# create a list to hold the blossom sprites
blossomList = pygame.sprite.Group()
# create a list that holds all sprites
spriteList = pygame.sprite.Group()

# create the fruits and the blossoms
numberFruits = 10
numberBlossoms = 3
for i in range(0, numberFruits):
    blawesomeFruit = Fruit(10, 10, GREEN, 2)
    fruitList.add(blawesomeFruit)
    spriteList.add(blawesomeFruit)
    for x in range(0, numberBlossoms):
        blawesomeBlossom = Blossom(blawesomeFruit)
        blossomList.add(blawesomeBlossom)
        spriteList.add(blawesomeBlossom)
# fruit_y = 10
# fruit_x = 10
#displaying tree to background
#screen.fill(color)


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

    # update the current time
    currentTime = pygame.time.get_ticks()
    # game logic can go here
    spriteList.update()
    # fill the background of the game
    display_surface.fill ((0, 0, 0))

    # draw to the screen

    spriteList.draw(display_surface)
    # 
    # pygame.draw.rect(display_surface, color, (fruit_x + 70, fruit_y + 10, 20, 20))
    # pygame.draw.rect(display_surface, color, (fruit_x + 180, fruit_y + 18, 20, 20))
    # display_surface.blit(image,(0,0))
    # display_surface.blit(carrot, (10,10))
    # fruit_y = fruit_y + 5

    # update display
    pygame.display.flip()
    clock.tick(60)
