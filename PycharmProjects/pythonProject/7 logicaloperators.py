# logical operators (and,or,not) = used to check if two or more conditional statements are true

temp = int(input("What is the temperature outside?: ")) #cast as int data type

if not(temp >= 0 and temp <= 30):
    print("The temperature today is not good!")
    print("Stay inside!")

elif not(temp <0 or temp >30):
    print("The temperature today is good!")
    print("Go outside!")

