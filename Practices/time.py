# IM Time

time = int(input("time of day in military time: "))

if time <= 12:
    print("goodmorning!")
elif time <= 18:
    print("good afteernoon!")
elif time <= 20:
    print("good evening")
else:
    print("good night!")