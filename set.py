set1={"yellow","green","orange","orange"}
set2={"red","blue","green"}
print(set1)


list1=[1,2,3,4,5]
x=set(list1)
print(x)
#union
print(set1|(set2))
#intersection
print(set1&(set2))
#difference
print(set1-set2)
#symmetric difference
print(set1^(set2))
set1.add("purple")
print(set1)
set1.update("black")
print(set1)
set1.discard("white")
print(set1)
set1.remove("green")
print(set1)
set1.add("teal")
print(set1)
set1.remove("grey")
print(set1)