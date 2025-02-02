tuple1=("John",95,"UK",["tennis","reading"])
tuple2=("math","white tea","piano","piano")

#unpacking a tuple
name,marks,location,hobbies=tuple1
print(f"Johns marks are {marks}")
print(f"{name}**{marks}**{location}")

for i in tuple1:
    print(i,end="**")
print()
print(hobbies[1])
print(name[2])
print(hobbies[1][0])
print(tuple1[2][1])

print(tuple1[2:])
print(tuple1[1:3])
tuple1[3].append("writing")
print(tuple1[3])
tuple1[3][2]="cricket"
print(tuple1[3])

tuple3=(tuple1+tuple2)
print(tuple3)
print(tuple2.index("piano"))
print(tuple2.count("piano"))



tuple1=("a")
print(tuple1)
