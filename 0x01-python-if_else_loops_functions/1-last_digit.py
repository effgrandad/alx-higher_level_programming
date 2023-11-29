#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
if number < 0:
    digit = -(digit)
string = "digit of {} is {}".format(number, digit)
if digit > 5:
    print(f"{string} and is greater than 5")
elif digit == 0:
    print(f"{string} and is 0")
elif digit < 0:
    print(f"{string} and is less than 6 and not 0")
