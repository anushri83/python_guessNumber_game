import random   
random_number=random.randint(1,100)   #Generate a random number between 1 to 100
while True:
    num=input("Guess a number from 1 to 100 or Quit: ")  #Take input from user
    if (num=="Quit"):
        break
    num=int(num)
    if (num==random_number):
        print("your guessed a correct number")
        break
    elif (num > random_number):
        print("your guessed a larger number,Guess again")
    else :
        print("your guessed a smaller number,Guess again")

print("____GAMEOVER____")
