import pygame, sys
from src.utils import load_image
from src.ship import Ship

class Game:
  def __init__(self):
    ship_sprite = Ship(assets['ship'], (WIDTH / 2, 535), screen)
    self.ship = pygame.sprite.GroupSingle(ship_sprite)
    
  def run(self): 
    self.ship.update()
    
    self.ship.sprite.lasers.draw(screen)
    self.ship.draw(screen)
    
if __name__ == '__main__':
  pygame.init()
  
  WIDTH = 800
  HEIGHT = 600
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  
  pygame.display.set_caption('Asteroids')
  
  FPS = 60
  clock = pygame.time.Clock()
  
  assets = {
      'ship': load_image('ship.png'),
      'asteroid': load_image('asteroid.png'),
    }
  
  game = Game()
  
  while True:
      screen.fill((0,0,0))
      game.run()
            
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

      pygame.display.update()
      clock.tick(FPS)
  