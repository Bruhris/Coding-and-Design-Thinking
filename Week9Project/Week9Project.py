import pygame
import random
import math

from pygame.constants import KEYDOWN

# Initialize pygame

pygame.init()

S_WIDTH = 800
S_HEIGHT = 800

# Initialize images

imp1 = pygame.image.load('Week9Project/img/imposter1.png')
imp2 = pygame.image.load('Week9Project/img/imposter2.png')
imp3 = pygame.image.load('Week9Project/img/imposter3.png')
imp4 = pygame.image.load('Week9Project/img/imposter4.png')
imp5 = pygame.image.load('Week9Project/img/imposter5.png')

imps = [imp1, imp2, imp3, imp4, imp5]

# Title and icon of window

pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('Week9Project/img/icon.png')
pygame.display.set_icon(icon)

# Create the screen and set the background
screen = pygame.display.set_mode((S_WIDTH,S_HEIGHT))
background = pygame.image.load('Week9Project/img/background.jpg')


class Player():
    img = pygame.image.load('Week9Project/img/player.png')
    img = pygame.transform.scale(img, (55,57))
    WIDTH = img.get_width()
    HEIGHT = img.get_height()

    def __init__(self):
        self.x = S_WIDTH / 2 - self.WIDTH /2
        self.y = S_HEIGHT - self.HEIGHT * 1.5
        self.x_movement = 0
    
    def move_right(self):
        self.x_movement = 3.5

    def move_left(self):
        self.x_movement = -3.5
    
    def stop_moving(self):
        self.x_movement = 0

    def update(self):
        self.x += self.x_movement
        self.boundary_check()
        screen.blit(self.img, (self.x, self.y))

    def boundary_check(self):
        if self.x <= 0:
            self.x = 0
        elif self.x >= S_WIDTH - self.WIDTH:
            self.x = S_WIDTH - self.WIDTH

class Invader():
    img = random.choice(imps)
    img = pygame.transform.scale(img, (55,60))
    WIDTH = img.get_width()
    HEIGHT = img.get_height()
    y_shift = S_HEIGHT * 0.05

    def __init__(self):
        self.x = random.randint(0, S_WIDTH - self.WIDTH)
        self.y = random.randint(int(S_HEIGHT * 0.0625), int(S_HEIGHT * 0.25))
        self.x_movement = 3
    
    def update(self):
        self.x += self.x_movement
        self.boundary_check()
        screen.blit(self.img, (self.x, self.y))

    def boundary_check(self):
        if self.x <= 0:
            self.x_movement =  3
            self.y += self.y_shift
        elif self.x >= S_WIDTH - self.WIDTH:
            self.x_movement = -3
            self.y += self.y_shift

player = Player()
num_invaders = 5
invaders = [Invader() for i in range(num_invaders)]

# Game loop
loop = True
while loop:

    screen.fill((0,0,0))
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.move_left()
            if event.key == pygame.K_d:
                player.move_right()    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player.stop_moving()

    player.update()
    for invader in invaders: # Updates every invader
        invader.update()
    pygame.display.update()

