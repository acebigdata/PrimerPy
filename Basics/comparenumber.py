import pandas as pd
import random

guess_number = int(round(random.random() * 100, ndigits=0))

print("Enter a Number: ")
input_number = int(input())

while input_number != guess_number:
    if input_number > guess_number:
        print("Your number is larger, guess again: ")
        input_number = int(input())
    else:
        print("Your number is smaller, guess again: ")
        input_number = int(input())

print("Your guess is right!")
