#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
if number < 0:
    lastdigit = -lastdigit
print(f"Last digit of {number:d} is {digit:d} and is", end="")
if lastdigit > 5:
    print(f" greater than 5")
elif lastdigit == 0:
    print(f"is 0")
else:
    print(" than 6 not 0")
