import pygame
import sys
from gameobject import *
from board import *
from score import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

tmr = 0
direction = ""
reset = False

gameover_image = pygame.image.load("images/dead.png")

def main():
  global tmr, direction, reset

  pygame.init()
  pygame.display.set_caption("Square of Square (SOS)")
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()

  root = GameObject(0, 0)
  GameObject.root = root

  board = Board(100, 100, 150, 150, 10)
  root.children.append(board)

  text = Text(0, 0, "Text")
  root.children.append(text)

  score = Score(SCREEN_WIDTH / 2, 50, (255, 255, 255), 80)
  text.children.append(score)

  max_score = Maxscore(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50, (255, 255, 255), 80, score, board)
  text.children.append(max_score)

  for i in range(board.row):
    for j in range(board.col):
      tile = Tile(board.x + j * board.width + board.width / 2, board.y + i * board.height + board.height / 2, 0, int(board.width / 3) if board.width < board.height else int(board.height / 3))
      root.children.append(tile)
      board.children.append(tile)

  while True:
    tmr = tmr + 1
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        max_score = max_score.max_score
        with open('txt/BestScore.txt', 'w') as file:
          file.write(str(max_score))
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F1:
          screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
        if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
          screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.draw.rect(screen, (0, 0, 0), [0, 0, SCREEN_WIDTH, SCREEN_HEIGHT])

    key = pygame.key.get_pressed()
    root.key_input(key)

    score.score = sum([sum(data) for data in board.board_data])
    root.update()
    root.draw(screen)
    if board.gameover:
      screen.blit(gameover_image, [0, 0])

    pygame.display.update()
    clock.tick(30)

if __name__ == '__main__':
  main()
