#if statements are block of code that will execute if it's condition is true.

age = int(input ("How old are you?: ")) #make int data type so it accepts numbers because of it being a string.

if age == 100:
    print("You are very old!")
elif age >= 18:
    print("You are an adult!")
elif age < 0: #else if statement
    print("You haven't been born yet!")
else: #if all over statements are not true
    print("You are a child!")

