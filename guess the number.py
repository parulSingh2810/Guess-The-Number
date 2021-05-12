# exercise, number guessing game
#  Make a variable  like winning number and assign any number 
#  ask user to guess number 
#  if user guessed correct then print "ohkayyy  *** you win the game  XD XD XD ENJOY******"
#  if user didn't guessed  correctly then :
#      if user guessed lower number the print " toooo low , guess higher number "
#      if user guessed higher  than the actual number then print" tooo highhh , guesss something lower babe"

#      also include rsandom number to generate random winning number
from random import randint
winning_number = randint(1,20)
print(winning_number)
guess = 1
n = int(input("Guess a number B/W 1 to 20: "))
gameover = False

while not gameover:
    if n == winning_number:
        print(f"congrats, you win XD XD XD and you guessed this number in {guess} times")
        gameover = true       
       
    elif n< winning_number:
        print("toooo low , guess something higher number :( :( :( :( :( :(")
        guess += 1

        number = int(input("guess again:"))
    else:
        print("tooo highhh , guesss something lower babe :( :( :( :( :( :(")
        guess += 1

        number = int(input("guess again:"))

        
     

  