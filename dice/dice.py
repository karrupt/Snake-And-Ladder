import pygame
import random
from pygame import mixer

# loading the dice onto the display
def throw_dice():
    dice_roll = mixer.Sound('audio/dice_roll.mp3') # whenever dice is rolled this sound plays
    dice_roll.play()
    num = random.randint(1, 6)
    if num == 1:
        dice = pygame.image.load("dice/1.png")
    elif num == 2:
        dice = pygame.image.load("dice/2.png")
    elif num == 3:
        dice = pygame.image.load("dice/3.png")
    elif num == 4:
        dice = pygame.image.load("dice/4.png")
    elif num == 5:
        dice = pygame.image.load("dice/5.png")
    elif num == 6:
        dice = pygame.image.load("dice/6.png")
    return (dice, num)