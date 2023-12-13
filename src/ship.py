import pygame
from pygame.math import Vector2

class Ship(pygame.sprite.Sprite):
  def __init__(self, image, pos, screen):
    super().__init__()
    #drawing info
    self.screen = screen
    self.image = image
    self.rect = self.image.get_rect(center= pos)
    
    #physics
    self.direction = pygame.math.Vector2(0,0)
    self.speed = 2
    self.gravity = -0.8
    
  def get_input(self):
    keys = pygame.key.get_pressed()

    #movement
    if keys[pygame.K_LEFT]:
      self.direction.x = -1
    elif keys[pygame.K_RIGHT]:
      self.direction.x = 1
    else:
      self.direction.x = 0
      
    if keys[pygame.K_UP]:
      self.direction.y = -1
    elif keys[pygame.K_DOWN]:
      self.direction.y = 1
    else:
      self.direction.y = 0
    
    #normalize vector
    if self.direction.x != 0 or self.direction.y != 0:
      self.direction.scale_to_length(4)
      self.rect.x += self.direction.x * self.speed
      self.rect.y += self.direction.y * self.speed
      
  def collision(self):
    # collision with screen
    if self.rect.left <= 0:
      self.rect.left = 0
    elif self.rect.right >= self.screen.get_width():
      self.rect.right = 800
    elif self.rect.top <= 0:
      self.rect.top = 0
    elif self.rect.bottom >= self.screen.get_height():
      self.rect.bottom = 600
  
  def update(self):
    self.get_input()
    self.collision()
      
  
