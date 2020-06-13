'''
Sam Minix
6/3/20

Handles the gameplay of blocks sliding back and forth
'''
import time
import display
import random
import sys
import select

global play
def game(list_of_rows, rowNum, blockNum):

  forward = random.choice([True, False]) #to randomize start side
  play = False
  while True:
    if forward == True:
      for i in range(7 - blockNum): #these statements slide the blocks back and forth
        copy = list_of_rows[:] #make a copy to not change original game state
        index = i+1
        currRow = copy[rowNum]
        change = ['#'] * blockNum
        currRow = currRow[:index] + change + currRow[blockNum+index:]
        copy[rowNum] = currRow
        display.display(copy)
        
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]: #test for user input from: https://stackoverflow.com/questions/22391134/exiting-while-loop-by-pressing-enter-without-blocking-how-can-i-improve-this-me/22391379#22391379
          line = input()
          play = True #if there is input, play is to to start next row
          break  
      if play:
        break
      forward = False #flip direction 
      continue
    
    else: #this else statement is very similar to forward if, might be able to simplify in a function
      for j in reversed(range(7 - blockNum)): #reverses blocks so they go other direction
        copy = list_of_rows[:] 
        index = j+2
        currRow = list_of_rows[rowNum]
        change = ['#'] * blockNum
        currRow = currRow[:index] + change + currRow[index+blockNum:]
        copy[rowNum] = currRow
        display.display(copy)
        
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
          line = input()
          play = True
          break
        
      if play:
        break
      forward = True

  

  if rowNum != 14: #when player inputs, break out while loop and check placement
    prevRow = list_of_rows[rowNum+1]
    for i in range(9):
      if currRow[i] == '#' and prevRow[i] != '#': #if nothing below block
        currRow[i] = ' ' #leave a blank space and reduce number of blocks
        blockNum -= 1

  if blockNum == 0:#failure
    print("lose")
    sys.exit()
  elif rowNum == 0: #goal
    print("win")
    sys.exit()
  else:
    game(copy, rowNum - 1, blockNum) #next row

    
