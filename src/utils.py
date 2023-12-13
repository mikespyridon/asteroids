import pygame

BASE_IMG_PATH = 'assets/images/'

def load_image(path):
  img = pygame.image.load(BASE_IMG_PATH + path).convert()
  if path == 'ship.png':
    img = pygame.transform.scale(img, [70,70])
  return img
