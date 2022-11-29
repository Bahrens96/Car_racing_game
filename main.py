#Car Racing Game
#Inspired by Tech with Tim | https://www.youtube.com/watch?v=L3ktUWfAMPg
#11/28/22
#On Part 1 @25:10

import pygame
import time
import math
from utils import scale_image



#load the images in
GRASS = scale_image(pygame.image.load("images/lawn.png"),2.5)
TRACK = scale_image(pygame.image.load("images/track_small.png"),1.1)

TRACK_BORDER = scale_image(pygame.image.load("images/track_outline_small.png"),1.1)
FINISH = scale_image(pygame.image.load("images/finish_line.png"),.1)

RED_CAR = scale_image(pygame.image.load("images/red_car_small.png"),.05)
GREEN_CAR = scale_image(pygame.image.load("images/green_car_small.png"),.03)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game!")

#display images
FPS = 60

class Abstract_Car:
    def __init__(self,max_vel,rotation_vel):
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
    
    def rotate(self,left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

        

        

def draw(win,images):
    for img,pos in images:
        win.blit(img,pos)


run = True
clock = pygame.time.Clock()
images = [(GRASS, (0,0)),(TRACK, (0,0))]

while run:
    clock.tick(FPS)

    draw(WIN,images)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
pygame.quit()   