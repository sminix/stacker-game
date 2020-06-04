'''
Sam Minix
6/3/20

Handles the gameplay of blocks sliding back and forth
'''
import time
import display
def game(list_of_rows, rowNum, blockNum):
  forward = True #random.choice([True, False] to randomize start location
  while True:
    if forward == True:
      for i in range(8 - blockNum):
        copy = list_of_rows[:]
        index = i+1
        currRow = copy[rowNum]
        change = ['#'] * blockNum
        currRow = currRow[:index] + change + currRow[blockNum+index:]
        time.sleep(1)
        copy[rowNum] = currRow
        display.display(copy)
      forward = False
      continue
    else:
      for j in reversed(range(6 - blockNum)):
        copy = list_of_rows[:]
        index = j+2
        currRow = list_of_rows[rowNum]
        change = ['#'] * blockNum
        currRow = currRow[:index] + change + currRow[index+blockNum:]
        copy[rowNum] = currRow
        time.sleep(1)
        display.display(copy)
      forward = True

    