'''
Sam Minix
6/4/20

Controls the terminal display using curses
'''
import sys
import time

def display(gameState):
  time.sleep(.5)
  sys.stdout.write("\x1b[f\x1b[J") #clears output and sets cursor in top corner from https://stackoverflow.com/questions/51315269/multithreading-curses-output-in-python
  for i in range(15): 
    for j in range(9):
      sys.stdout.write(str(gameState[i][j]))
    if i == 0:
      sys.stdout.write(" Major Prize!")
    if i == 5:
      sys.stdout.write(" Minor Prize")
    if i == 14:
      sys.stdout.write("Start")
    sys.stdout.write('\n')
    sys.stdout.flush() #flushes output before next row


