import pygame
from gameobject import *

ORANGE = (255, 187, 0)
GREEN = (171, 242, 0)
BLUE = (72, 156, 255)
PURPLE = (203, 108, 255)
BLACK = (54, 54, 54)

class Tile(GameObject):
  def __init__(self, tile_x, tile_y, number, radius):
    super().__init__(tile_x, tile_y, "Tile")
    self.number = number
    self.visible = self.number > 0
    self.radius = radius
    self.colors = [
      ORANGE,
      GREEN,
      BLUE,
      PURPLE
    ]
  
  def update(self):
    self.visible = self.number > 0

  def draw(self, screen):
    if self.visible:
      pygame.draw.circle(screen, self.colors[self.setColorNum(self.number) % 4], [self.x, self.y], self.radius)
      font = pygame.font.Font(None, self.radius).render(str(self.number), True, BLACK)
      screen.blit(font, [self.x - font.get_width() / 2, self.y - font.get_height() / 2])
  
  def setInformation(self, x, y, number):
    self.x = x
    self.y = y
    self.number = number
  
  def setColorNum(self, number):
    num, n = number, 0
    while (not num == 0): num, n = num / 2, n + 1
    return n
