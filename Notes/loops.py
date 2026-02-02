import random #library code someone else wrote, always import at the top
start = 1

while start <= 20:
    print(start)
    start += 1

goose = random.randint(1,20)
count = 1

while count < goose:
    print("Duck")
    count += 1
print("GOOSE!")

number = random.randit(1,25)

while True:
    guess = int(input("guess a number between 1 and 25: "))
    if guess == number:
        print(f"congradulations! {number} was the number")
        break #exit the loop 
    elif guess > 25 or guess < 1:
        print("that isn't an option.")
    