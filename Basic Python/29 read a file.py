# reading a file in Python
# read contents from a file and print to the console

try:
    with open("folder/test.txt") as file: # you'll do this if on here, for other location, filepath with \\
        print(file.read())
except FileNotFoundError: #instead of printing error, this returns a printed statement instead
    print("That file was not found.")

#print(file.closed) # if file is closed, it will print true and vice versa

