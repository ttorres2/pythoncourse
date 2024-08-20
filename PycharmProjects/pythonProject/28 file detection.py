import os

#checking to see if a file exists somewhere on our computer.

path = "C:\\Users\\ttorres"

if os.path.exists(path):
    print("That location exists.")
    if os.path.isfile(path):
        print("That is a file.")
    elif os.path.isdir(path): #to see if its a directory (folder)
        print("That is a directory.")
else:
    print("That location does not exist.")

