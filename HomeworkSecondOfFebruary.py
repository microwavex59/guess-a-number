fruits={"Apple":50,"Banana":30,"Watermelon":40,"Orange":60,"Strawberry":20}
fruits["Apple"]=55
fruits["mango"]=75
fruits["grape"]=85
search=input("What item do you want")
if search in fruits:
    print(fruits[search])
else:
    print("Item not found")
for i in fruits.keys():
    print(i,fruits[i])