import pygame
import sys
import os

from Components.player import Player
from Components.camera import Camera

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

WIDTH, HEIGHT = 990, 540

FPS = 30

# general colours
BLACK =  (  0,   0,   0)
WHITE =  (255, 255, 255)
RED =    (211,   0,   0)
GREEN =  (  0, 150,   0)
DGREEN = (  0, 100,   0)
BLUE =   (  0,   0, 211)
LBLUE =  (137, 207, 240)
GREY =   (201, 201, 201)
LGREY =  (231, 231, 231)
DGREY =  ( 50,  50,  50)
LBROWN = (185, 122,  87)
DBROWN = (159, 100,  64)

# padding is relative to width
PADDING = WIDTH/(990/20)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Station 12")

station_camera = Camera()
player = Player(station_camera, (0, 0))

clock = pygame.time.Clock()
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  WIN.fill(GREEN)
  
  station_camera.update()
  station_camera.custom_draw(player)
  
  pygame.display.update()
  
  clock.tick(FPS)