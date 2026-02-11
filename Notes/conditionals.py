number = 42

if number < 10 and number > -10:
     print(f"{number} is a single digit number")
elif abs(number) < 100:
    print(f"{number} is a double digit number")
else:
    print(f"{number} is a triple digit number")
     
print("end of the program") 