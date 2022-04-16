# import pygame package
import pygame
import sys
import random

# initializing imported module
pygame.init()

# displaying a window of height
# 500 and width 400
display_surface = pygame.display.set_mode((850, 600))
#screen = pygame.display.set_mode((850, 600))
#Making background image
#image = pygame.image.load('tree.png')
carrot = pygame.image.load('carrot.png')
# Initialing RGB Color 
color = (255,0, 0)
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
    display_surface.fill ((0, 0, 0))
    pygame.draw.rect(display_surface, color, (fruit_x, fruit_y, 20, 20))
    #pygame.draw.rect(display_surface, color, (fruit_x + 40, fruit_y, 20, 20))
    #pygame.draw.rect(display_surface, color, (fruit_x + 80, fruit_y, 20, 20))
    #display_surface.blit(image,(0,0))
    #display_surface.blit(carrot, (10,10))
    #update display

    fruit_y = fruit_y + 11

    pygame.display.flip()
    clock.tick(60)
