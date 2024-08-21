# index operator [] = gives access to a sequence's element (str, list, tuples)

name = "bro Code!"

#checks to see if first letter is lower case, if it is, then it capitalizes it.
if(name[0].islower()):
    name = name.capitalize() #changes to variable with a capitalize function.

#create substrings using index operator
first_name = name [:3].upper()
last_name = name [4:8].lower()
last_character = name [-1]

print(name)
print(first_name)
print(last_name)
print(last_character)

