import pygame
from random import randint, randrange

BASE_IMG_PATH = 'assets/images/'

def load_image(path):
  img = pygame.image.load(BASE_IMG_PATH + path).convert()
  if path == 'ship.png':
    img = pygame.transform.scale(img, [70,70])
    img.set_colorkey((0,0,0))
  if path == 'asteroid.png':
    num = randint(50, 100)
    img = pygame.transform.scale(img, [num, num])
    img.set_colorkey((0,0,0))
  if path == 'background.jpg':
    img = pygame.transform.scale(img, [800,600])
  return img
