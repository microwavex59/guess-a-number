#print value of index 1
#n=[1,2,3]
#print(n[1])

list1=[]
for i in range(5):
    a=int(input("Input a number  "))
    list1.append(a)
print(list1)

search=int(input("Enter number you want to find  "))
for j in range(5):
    if list1[j]==search:
        print("number found")
        break

else:
    print("Number not found")


