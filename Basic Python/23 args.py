# *args = parameter that will pack all arguments into a tuple.
#         useful so that a function can accepy a varying amount of arguments.

def add(*stuff): #passing all arguments into a tuple.
    sum = 0
    stuff = list(stuff) #casts tuple as a list
    stuff[0] = 0 # to change a value
    for i in stuff:
        sum += i
    return sum #adds all args together

print(add(1,2,3,4,5,6)) #since there are 3 arguments within it and only 2 defined above, you can pass *args ^