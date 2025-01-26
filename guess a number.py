import random
def guess_number():
    x=random.randint(1,10)
    for i in range(5):
        guess=int(input("Guess a number"))
        if guess==x:
            print("good job")
        elif guess<x:
            print("guess a higher number")
        elif guess>x:
            print("guess a lower number")
        
guess_number()