import random #import this to have access to random module

x = random.randint(1,6) #random number between 1 and 6
y = random.random() #random floating number between 0 and 1.

myList = ["rock","paper","scissors"]
z = random.choice(myList)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)

print(x)
print(y)
print(z)
print(cards)
