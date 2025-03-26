# Number Guessing game 
import random as rd
computerNo=rd.randrange(1,10)

while True:
    n=int(input('Guess the Number btw 1 and 10:'))
    if n==computerNo:
        print("Correct You Won the Game....")
        break
    elif n>computerNo:
        print("Guess no.is high actual no. is :",computerNo)
    elif n<computerNo:
        print("Guess no.is low actual no. is :",computerNo) 