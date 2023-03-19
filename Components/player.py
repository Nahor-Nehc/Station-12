import math
import pygame
import os

class Player(pygame.sprite.Sprite):
  def __init__(self, group, position):
    super().__init__(group)
    self.position = position
    self.image = pygame.Surface((100, 100))
    self.image.fill("#000000")
    self.rect = self.image.get_rect(center = self.position)
    
    self.direction = pygame.math.Vector2()
    self.default_speed = 5
    self.speed = self.default_speed
  
  def input(self):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
      self.direction.y = -1
    elif keys[pygame.K_DOWN]:
      self.direction.y = 1
    else:
      self.direction.y = 0
    
    if keys[pygame.K_RIGHT]:
      self.direction.x = 1
    elif keys[pygame.K_LEFT]:
      self.direction.x = -1
    else:
      self.direction.x = 0
      
    if self.direction.x * self.direction.y == 0:
      self.speed = self.default_speed
    else:
      self.speed = self.default_speed / math.sqrt(2)
  
  def update(self):
    self.input()
    print(self.speed)
    self.rect.center += self.direction * self.speed