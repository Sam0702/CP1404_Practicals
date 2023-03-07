from random import random

score = float(input("Enter score: "))
if score >= 0 and score <= 100:
    if score > 90:
        print("Excellent")
    elif score > 50:
        print("Pass")
    elif score < 50:
        print("Bad")
else:
    print("Inclusive")