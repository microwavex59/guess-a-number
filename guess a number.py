'''import random
def guess_number():
    x=random.randint(1,10)
    for i in range(5):
        guess=int(input("Guess a number"))
        if guess==x:
            print("good job")
            break
        elif guess<x:
            print("guess a higher number")
        elif guess>x:
            print("guess a lower number")
        
guess_number()'''
#find length of dicitonary
dictionary1={"India":"rupee", "japan":"yen", "united states":"dollar"}
print(dictionary1)
#find length of dicitonary
print(len(dictionary1))
dictionary1["japan"]="YEN"
print(dictionary1)
dictionary1["China"]="Yuan"
print(dictionary1)
dictionary1["currencies"]=["dollar","yuan","etc"]
print(dictionary1)