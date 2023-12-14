import pygame
from src.laser import Laser

class Ship(pygame.sprite.Sprite):
  def __init__(self, image, pos, screen):
    super().__init__()
    #drawing info
    self.screen = screen
    self.image = image
    self.rect = self.image.get_rect(center= pos)
    
    #laser properties
    self.ready_to_shoot = True
    self.laser_time = 0
    self.laser_cooldown = 100
    
    self.lasers = pygame.sprite.Group()
    
    #physics
    self.direction = pygame.math.Vector2(0,0)
    self.speed = 2
    
    self.health = 3
    
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
    
    if keys[pygame.K_SPACE] and self.ready_to_shoot:
      self.shoot_laser()
      self.ready_to_shoot = False
      self.laser_time = pygame.time.get_ticks()
    
    #normalize vector
    if self.direction.x != 0 or self.direction.y != 0:
      self.direction.scale_to_length(4)
      self.rect.x += self.direction.x * self.speed
      self.rect.y += self.direction.y * self.speed
      
  def recharge(self):
    if not self.ready_to_shoot:
      current_time = pygame.time.get_ticks()
      if current_time - self.laser_time >= self.laser_cooldown:
        self.ready_to_shoot = True
        
  def shoot_laser(self):
    self.lasers.add(Laser(pygame.Surface((3, 40)), self.rect.center))
    
  def screen_constraint(self):
    #horizontal screen collison
    if self.rect.left <= 0:
      self.rect.left = 0
    elif self.rect.right >= 800:
      self.rect.right = 800
     
     #vertical screen collision 
    if self.rect.top <= 400:
      self.rect.top = 400
    elif self.rect.bottom >= 600:
      self.rect.bottom = 600
  
  def get_hit(self):
    
    if self.health <= 0:
      self.kill()
    else: 
      self.health -= 1
  
  def update(self):
    self.get_input()
    self.screen_constraint()
    self.recharge()
    self.lasers.update()
      