text = "Have a nice day!\nSee ya!"

with open ("folder/test.txt", "a") as file: # r for read, or w for write, a for append
    file.write(text) #writes to the test.txt file