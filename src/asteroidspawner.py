import pygame
from src.asteroid import Asteroids
from src.utils import load_image

import random

class AsteroidSpawner:
  def __init__(self):
    self.asteroid_group = pygame.sprite.Group()
    self.spawn_timer = random.randrange(30, 60)
       
  def update(self):
    self.asteroid_group.update()
    self.spawn_timer -= 1
    if self.spawn_timer == 0:
      self.spawn_asteroid()
      self.spawn_timer = random.randrange(30, 60)
      
  def spawn_asteroid(self):
    new_asteroid = Asteroids((random.randint(100, 700), random.randint(-50, -20)))
    self.asteroid_group.add(new_asteroid)