# list = used to store multiple items in a single variable.

food = ["pizza","cheeseburger","hot dog","spaghetti"] # square brackets create a list.
print(food[0]) # will print position number element in list.

food[0] = "Sushi" # replaces position 0 in list with sushi.
print(food[0])

food.append("ice cream") #appends ice cream at the end of the food list.
food.remove("hot dog") #removes hot dog from the list.
food.pop() #will remove the last element.
food.insert(0,"cake") #will add cake as position 0.
food.sort() #will list alphabetically.
food.clear() #this will remove all elements of a list.

for x in food:
    print(x) # will print all elements found in list 'food'.