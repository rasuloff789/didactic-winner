import random

n = random.randint(0,     10)
quess = int(input("guess a number between 0 and 10: "))
guesses = 0

while True:
    if n == guess:
        print("Topdingingiz!")
        break
    else:
        guesses += 1

    print("Xato, qayta urining!")
    if guesses >= 3:
        print("Yutqazdingiz!")
        break
