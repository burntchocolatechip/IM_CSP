numbers =[3,5,2,4,5,2,4,6,3,3,]
name = ["Alex", "Katie", "Vienna"]

name[0] = "Erick"
names.append("Jayshree") #adds to end of the list
index = names.index("Vienna")
names.pop(index)
print(len(names))
print(names)

for name in names:
    print(f"Hello" [name])

for number in numbers:
    print(f"{number} - 10 = {number-10}")

for i in range(20):
    print(f"this is the {i} iteration of this loop")