#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number == 0:
    print(f"{number} is zero")
# checking if our random number is greater than zero
elif number > 0:
    print(f"{number} is positive")
# checking if our random number is less than zero
else:
    print(f"{number} is negative")
