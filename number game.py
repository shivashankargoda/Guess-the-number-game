import random
number=random.randrange(1,50)
guess=int(input("Gues a number between 1 and 50:"))
while guess!=number:
    if guess<number:
        print("You need to guess higher Try again")
        guess=int(input("\n Guess a number between 1 and 50:"))

    else:
        print("You need to guess lower. Try again")
        guess=int(input("\n Guess a number between 1 and 50:"))
print ("you guessed the number correctly:")