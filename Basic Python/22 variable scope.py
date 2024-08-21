# scope = The region that a variable is recognized.
#         A variable is only available from inside the region it is created.
#         A global and locally scoped version of a variable can be created.

name = "Bro" # global scope (variable that is available inside and outside functions)

def display_name(): # creates function called display_name
    name = "Code" # local scope (available only inside this function)
    print (name)

display_name() # prints local variable
print(name) # prints global variable
