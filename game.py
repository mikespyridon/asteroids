import pygame, sys
from src.utils import load_image
from src.ship import Ship
from src.asteroidspawner import AsteroidSpawner
import math

class Game:
  def __init__(self):
    ship_sprite = Ship(assets['ship'], (WIDTH / 2, 535), screen)
    self.ship = pygame.sprite.GroupSingle(ship_sprite)
    self.asteroid_spawner = AsteroidSpawner()
    self.score = 0
    
    self.font = pygame.font.SysFont('Arial', 30)
    
  def draw_text(self, text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))
  
  def run(self): 
    
    self.draw_text(f'Score: {self.score}', self.font, 'white', 10, 10)
    self.ship.update()
    self.asteroid_spawner.update()
    
    self.ship.sprite.lasers.draw(screen)
    self.asteroid_spawner.asteroid_group.draw(screen)
    self.ship.draw(screen)
    
    self.collided = pygame.sprite.groupcollide(self.ship.sprite.lasers, self.asteroid_spawner.asteroid_group, True, False)
    #self.ship_collision = pygame.sprite.groupcollide(self.ship, self.asteroid_spawner.asteroid_group, True, False)
    
    for laser, asteroid in self.collided.items():
      asteroid[0].get_hit()
      self.score += 1
    
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
      'background': load_image('background.jpg')
    }
  
  game = Game()
  
  while True:
      screen.blit(assets['background'], (0,0))
      game.run()
     
            
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

      pygame.display.update()
      clock.tick(FPS)
  