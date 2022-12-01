#Car Racing Game
#Inspired by Tech with Tim | https://www.youtube.com/watch?v=L3ktUWfAMPg
#11/28/22
#On Part 2 @0:00

import pygame
import time
import math
from utils import scale_image,blit_rotate_center



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
        self.vel = 0 #determines the speed of the car
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.img = self.IMG
        self.x, self.y = self.START_POS
        self.acceleration = 0.1
    
    def rotate(self,left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self,win):
        blit_rotate_center(win,self.img,(self.x,self.y),self.angle)

    def move_foward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel) # if the accerlation is greater than the max vel, it defaults to the max vel
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        #check yucky trig pic
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        #plus returns positive values, makes car go foward, minus returns negative values, makes car go backwards
        self.y += vertical
        self.x += horizontal

    def reduce_speed(self):
        self.vel = max(self.vel-self.acceleration /2,0) #if the value is negative we dont wanna go backwards
        self.move()

class Player_Car(Abstract_Car):
    IMG = RED_CAR
    START_POS = (100,200)

def draw(win,images,player_Car):
    for img,pos in images:
        win.blit(img,pos)

    player_car.draw(win)
    pygame.display.update()


run = True
clock = pygame.time.Clock()
images = [(GRASS, (0,0)),(TRACK, (0,0))]
player_car = Player_Car(4,4)#higher the number the faster

while run:
    clock.tick(FPS)

    draw(WIN,images,player_car)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()
    moved = False

    # rotating the car keys
    if keys[pygame.K_a]:
        player_car.rotate(left = True)
    if keys[pygame.K_d]:
        player_car.rotate(right = True)
    if keys[pygame.K_w]:
        moved = True
        player_car.move_foward()

    if not moved:
        player_car.reduce_speed()

    
pygame.quit()   