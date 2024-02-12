#author Jack Bell
#date 3/8/2022
#version 1.0
#
#Rock Paper Scissors game
#Two players

from random import choices


print("welcome to Rock Paper Scissors!")
print("let's begin...")

print("rules 1 do not use uppercase, 2 cover your eyes when the other player is inputing their hand")

name1 = input("player 1: whats your name ")
name2 = input("player 2: whats your name ")

print("hello", name1, "and", name2)
print(name2, "close your eyes")

choice1 = input("player 1 go first, enter 'r' for rock 'p' for paper and 's' for scissors: ")
print('great choice! now ask', name2, "to chose")
choice2 = input("now player 2, enter 'r' for rock 'p' for paper and 's' for scissors: ")

if choice1 == choice2: #the logic 
    print("you both chose the same ")
elif choice1 == "r" and choice2 == "s":
    print(name1, "win", name2, "lost")
elif choice1 == "r" and choice2 == "p":
    print(name1, "lose", name2, "win")
elif choice1 == "p" and choice2 == "r":
    print(name1, "win", name2, "lost")
elif choice1 == "p" and choice2 == "s":
    print(name1, "lose", name2, "win")
elif choice1 == "s" and choice2 == "p":
    print(name1, "win", name2, "lost")
elif choice1 == "s" and choice2 == "r":
    print(name1, "lose", name2, "win")

print("thanks for playing Rock Paper Scissors") #thanking the player 