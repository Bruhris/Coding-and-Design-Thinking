import pygame
import random
import math

# Initialize pygame

pygame.init()

# Title and icon of window

pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('Week9Project/img/icon.png')
pygame.display.set_icon(icon)

# Create the screen and set the background
screen = pygame.display.set_mode((800,800))
background = pygame.image.load('Week9Project/img/background.jpg')


