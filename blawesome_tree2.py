# import pygame package
from turtle import speed
import pygame
import sys
import random
from models.Blossom import Blossom
from models.Fruit import Fruit

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
# carrot = pygame.image.load('carrot.png')
# fruitBlossom = pygame.image.load('fruitblossom.png')

# color constants 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
# building the fruit class
#  class Fruit(pygame.sprite.Sprite):
# build the contructor

    

    # def update(self):
        # self.rect.y = self.rect.y + self.speed


# adding the blossom class for falling objects from fruit ((i think i named this backwards))

# Create the in-game scoreboard font
score = '0'
scoreFont = pygame.font.SysFont('Arial', 20)
scoreBoard = scoreFont.render(score, True, (255, 255, 255))


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
    blawesomeFruit = Fruit(10, 10, GREEN)
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
    display_surface.blit(scoreBoard, (15, 15))
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
