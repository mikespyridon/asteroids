import pygame
from src.utils import load_image

class Asteroids(pygame.sprite.Sprite):
  def __init__(self,pos):
    super(Asteroids, self).__init__()
    self.image = load_image('asteroid.png')
    self.pos = pos
    self.rect = self.image.get_rect(center=pos)
    self.speed = 5
    self.hp = 3
    
    self.score = 0
  
  def destroy(self):
    if self.rect.y >= 800:
      self.kill()
      
  def get_hit(self):
    if self.hp <= 0:
      self.kill()
      self.score += 1
    self.hp -= 1
  
  def update(self):
    self.rect.y += self.speed
    self.destroy()
    
      
    
  