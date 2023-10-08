import pygame
from gameobject import *

class Text(GameObject):
  def __init__(self, x, y, name):
    super().__init__(x, y, name)
  
  def update(self):
    for child in self.children:
      child.update()

  def draw(self, screen):
    for child in self.children:
      child.draw(screen)
  
  def drawText(self, screen, txt, txt_x, txt_y, color, size):
    font = pygame.font.Font(None, size).render(txt, True, color)
    screen.blit(font, [txt_x - font.get_width() / 2, txt_y - font.get_height() / 2])

class Score(Text):
  def __init__(self, x, y, color, size):
    super().__init__(x, y, "Score")
    self.score = 0
    self.color = color
    self.size = size
  
  def draw(self, screen):
    super().drawText(screen, "SCORE:" + str(self.score), self.x, self.y, self.color, self.size)

class Maxscore(Text):
  def __init__(self, x, y, color, size, score, board):
    super().__init__(x, y, "MaxScore")
    self.score = score
    self.max_score = self.getMaxScore()
    self.color = color
    self.size = size
    self.board = board
    self.timer = 0

  def update(self):
    if self.score.score > self.max_score:
      self.max_score = self.score.score
      
    if not self.board.gameover:
      self.timer = 0
    else:
      if self.getMaxScore() < self.max_score:
        self.timer += 1

  def draw(self, screen):
    if self.timer == 0 or self.timer % 30 >= 15:
      super().drawText(screen, "MAX_SCORE:" + str(self.max_score), self.x, self.y, self.color, self.size)
  
  def getMaxScore(self):
    with open('txt/BestScore.txt', 'r') as file:
      score = int(file.read())
    return score
