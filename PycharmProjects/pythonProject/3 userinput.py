#user input

name = input("What is your name?: ") #prompts for user input, they are able to press Enter, assigns input to a variable.
age = int(input("How old are you?: ")) #casts input to the int data type, otherwise it won't work.
height = float(input("How tall are you in inches?: ")) #casts input to the float data type.

print("Your name is "+name+".") #returns a response.
print("You are "+str(age)+" years old.") #returns a response.
print("You are "+str(height)+" inches tall.") #returns a response.