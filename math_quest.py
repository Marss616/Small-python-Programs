#author Jack Bell
#date 3/8/2022
#version 1.0
#
#math quest
from itertools import product


name = input("welcome to math quest: what is your name ") #getting the uesrs name
print(name)
times_table = int(input("which times table would you like to practice? (1-12)"))

print("Ok", name, " on a piece of paper, write down the,")
print(times_table, "times table from 1 to 12.  When you’re ready I’ll show you the answer so you can check your work")

i = 1

while True:
    isready = input("are you ready? (y/n) ")
    if isready == "y":
        break

while i<=12: #computeing the times table
    print(times_table, "X", i, "=", times_table * i)
    i = i+1

correct = input("did you get all of them correct? (y/n)")
if correct == "y":
    print("good job")
else:
    print("better luck next time")

print("thanks for playing math quest!") #thanking the user
