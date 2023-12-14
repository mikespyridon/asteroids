import pygame

class Laser(pygame.sprite.Sprite):
  def __init__(self, image, pos):
    super().__init__()
    self.image = image
    self.image.fill('red')
    self.rect = self.image.get_rect(center= pos)
    self.speed = 15
    
  def destroy(self):
    if self.rect.bottom <= 0:
      self.kill()
    
  def update(self):
    self.rect.y -= self.speed
    self.destroy()
   
    
  