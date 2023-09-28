import random
import pygame
from gameobject import *
from tile import *

WHITE = (219, 219, 219)
GREEN = (107, 153, 0)

class Board(GameObject):
  def __init__(self, x, y, width, height, thick):
    super().__init__(x, y, "Board")
    self.board_data = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    self.row = len(self.board_data)
    self.col = len(self.board_data[0])
    self.width = width
    self.height = height
    self.thick = thick
    self.direction = ""
    self.k_up = False
    self.k_down = False
    self.k_left = False
    self.k_right = False
    self.k_r = False
    self.board_data = self.setPosition(self.board_data)

  def key_input(self, key):
    self.direction = ""
    if not key[pygame.K_w]:
      self.k_up = False
    if key[pygame.K_w] and not self.k_up:
      self.k_up = True
      self.direction = "UP"
    if not key[pygame.K_s]:
      self.k_down = False
    if key[pygame.K_s] and not self.k_down:
      self.k_down = True
      self.direction = "DOWN"
    if not key[pygame.K_a]:
      self.k_left = False
    if key[pygame.K_a] and not self.k_left:
      self.k_left = True
      self.direction = "LEFT"
    if not key[pygame.K_d]:
      self.k_right = False
    if key[pygame.K_d] and not self.k_right:
      self.k_right = True
      self.direction = "RIGHT"

    if not key[pygame.K_r]:
      self.k_r = False
    if key[pygame.K_r] and not self.k_r:
      self.k_r = True
      self.board_data = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
      ]
      self.board_data = self.setPosition(self.board_data)
  
  def update(self):
    if not self.direction == "":
      self.board_data = self.changeBoardData(self.board_data)
    for i in range(len(self.children)):
      self.children[i].setInformation(self.children[i].x, self.children[i].y, self.board_data[i // 4][i % 4])

  def draw(self, screen):
    pygame.draw.rect(screen, GREEN, [self.x, self.y, self.width * self.col, self.height * self.row])
    for i in range(self.row):
      for j in range(self.col):
        rx = self.x + self.width * j
        ry = self.y + self.height * i
        pygame.draw.rect(screen, WHITE, [rx + self.thick, ry + self.thick, self.width - self.thick * 2, self.height - self.thick * 2])

  def setPosition(self, board_data):
    next_board_data = board_data
    rn = random.randint(0, self.row - 1)
    while not 0 in next_board_data[rn]:
      rn = random.randint(0, self.row - 1)
    cn = random.randint(0, self.col - 1)
    while not next_board_data[rn][cn] == 0:
      cn = random.randint(0, self.col - 1)
    next_board_data[rn][cn] = random.choice([2, 4])
    return next_board_data

  def changeBoardData(self, board_data):
    next_board_data = [[board_data[j][i] for i in range(self.row)] for j in range(self.col)]
    isChange = False
    if self.direction == "UP":
      for i in range(self.col):
        isChange = False
        for j in range(1, self.row):
          if not next_board_data[j][i] == 0:
            for l in range(j, 0, -1):
              if next_board_data[l - 1][i] == 0:
                next_board_data[l - 1][i] = next_board_data[l][i]
                next_board_data[l][i] = 0
              elif next_board_data[l - 1][i] == next_board_data[l][i] and not isChange:
                next_board_data[l - 1][i] *= 2
                next_board_data[l][i] = 0
                isChange = True
    elif self.direction == "DOWN":
      for i in range(self.col):
        isChange = False
        for j in range(self.row - 2, -1, -1):
          if not next_board_data[j][i] == 0:
            for l in range(j, self.row - 1, 1):
              if next_board_data[l + 1][i] == 0:
                next_board_data[l + 1][i] = next_board_data[l][i]
                next_board_data[l][i] = 0
              elif next_board_data[l + 1][i] == next_board_data[l][i] and not isChange:
                next_board_data[l + 1][i] *= 2
                next_board_data[l][i] = 0
                isChange = True
    elif self.direction == "LEFT":
      for i in range(self.row):
        isChange = False
        for j in range(1, self.col):
          if not next_board_data[i][j] == 0:
            for l in range(j, 0, -1):
              if next_board_data[i][l - 1] == 0:
                next_board_data[i][l - 1] = next_board_data[i][l]
                next_board_data[i][l] = 0
              elif next_board_data[i][l - 1] == next_board_data[i][l] and not isChange:
                next_board_data[i][l - 1] *= 2
                next_board_data[i][l] = 0
                isChange = True
    elif self.direction == "RIGHT":
      for i in range(self.row):
        isChange = False
        for j in range(self.col - 2, -1, -1):
          if not next_board_data[i][j] == 0:
            for l in range(j, self.col - 1, 1):
              if next_board_data[i][l + 1] == 0:
                next_board_data[i][l + 1] = next_board_data[i][l]
                next_board_data[i][l] = 0
              elif next_board_data[i][l + 1] == next_board_data[i][l] and not isChange:
                next_board_data[i][l + 1] *= 2
                next_board_data[i][l] = 0
                isChange = True

    if not board_data == next_board_data:
      next_board_data = self.setPosition(next_board_data)
    return next_board_data
