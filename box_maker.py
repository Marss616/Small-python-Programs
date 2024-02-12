#this program can create a box

#this section will gather the dimentions of the box
rows = int(input("how many rows range is 1 - 10: "))
cols = int(input("how many cols range is 1 - 10: "))

#the program will still work with a higher range
if rows > 10:
    print("range error, program should not work")
elif rows == 0:
    exit()
else:
    print("")

if cols > 10:
    print("range error, program should not work")
elif cols == 0:
    exit()
else:
    print('')

emptycols = cols - 2
print("*", end="")
for i in range(0, emptycols):
    print("*", end="")
print("*")
for row in range(1,rows-1):
    print("*", end="")
    for i in range(0, emptycols):
        print("*", end='')
    print("*")
print("*", end="")
for i in range(0, emptycols):
    print("*", end='')
print("*")

#says good bye to the user to mark the program in complete 
print("good bye")