'''
Sam Minix
6/4/20

Controls the terminal display using curses
'''

import time

def display(gameState):
  for i in range(15):
    for j in range(9):
      print(gameState[i][j], end='')
    if i == 0:
      print(" Major Prize!", end='')
    if i == 5:
      print(" Minor Prize", end='')
    if i == 14:
      print("Start", end='')
    print()


