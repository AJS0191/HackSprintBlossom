# import pygame package
import pygame
import sys
import random
#from settings import Settings
from basket import Basket
from Fruit import Fruit
from Blossom import Blossom
import game_functions as gf
from pygame import mixer
from pygame.locals import *

mixer.init()
ting = pygame.mixer.Sound("ping.wav")
def ping():
    pygame.mixer.Sound.play(ting)
    #pygame.mixer.music.stop()
def run_game():
    #mixer.init()
    mixer.music.load('MP3FY_-Gaslamp-Funworks.wav')
    mixer.music.play()
    WIDTH = 850
    HEIGHT = 600
    # initializing imported module
    pygame.init()
    score = 0
    scoreFont = pygame.font.SysFont('Arial', 60)
    scoreBoard = scoreFont.render(str(score), True, (255, 255, 255))

    color = (255,255,255)

    #ai_settings = Settings()
    clock = pygame.time.Clock()
    #Making background image
    tree_bg = pygame.image.load('tree1.png')
    # displaying a window of height
    # 500 and width 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    basket = Basket(screen)
    pygame.display.set_caption("Blawesome Tree")
    fruitList = pygame.sprite.Group()
    #fruitList.add(basket)
    blossomList = pygame.sprite.Group()
    for x in range(0, 10):
        blawesomFruit = Fruit(15, 15)
        fruitList.add(blawesomFruit)
        for i in range(0, 3):
            blawBlossom = Blossom(blawesomFruit)
            blossomList.add(blawBlossom)
    
    #if fruitList == pygame.sprite.spritecollide(basket, fruitList, True):
        #score += 1
    # keep game running till running is true
    
    while True:
        #if basket.rect.left > WIDTH:
            #basket.rect.right = 0
        #if Fruit.colliderect(basket):
            #score +=1
        caught = pygame.sprite.spritecollide(basket, blossomList, True)
        if caught:
            score +=1
            print(score)
            ping()
            scoreBoard = scoreFont.render(str(score), True, (255, 255, 255))
        if basket.rect.left < 0:
            basket.rect.left = 0
        if basket.rect.right > WIDTH:
            basket.rect.right = WIDTH
        currentTime = pygame.time.get_ticks()
        gf.check_events(basket)
        screen.blit(tree_bg,(0,0))
        fruitList.draw(screen)
        blossomList.draw(screen)
        fruitList.update()
        for blossom in blossomList:
            blossom.update(currentTime)
        basket.update()
        basket.blitme()
        screen.blit(scoreBoard, (15, 15))
        pygame.display.update()
        clock.tick(60)
        #print(currentTime)
run_game()
