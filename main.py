'''
Sam Minix
6/3/20

Make a stacker arcade game
'''

import game
import display
#Function to print rows and columns at the start of the game
def gameStart():
  list_of_rows = []
  for i in range(15):
    row = []
    for j in range(9):
      if j == 0 or j == 8:
        row.append("|")
      elif i == 0 or i == 5 or i == 14:
        row.append("_")
      else:
        row.append(" ")
    list_of_rows.append(row)


  display.display(list_of_rows)

  game.game(list_of_rows, 14, 3)




gameStart()
