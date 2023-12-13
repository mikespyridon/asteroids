import pygame

class Laser(pygame.sprite.Sprite):
  def __init__(self, image, pos):
    super().__init__()
    self.image = image
    self.image.fill('red')
    self.rect = self.image.get_rect(center= pos)