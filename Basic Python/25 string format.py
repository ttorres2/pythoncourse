# str.format() = optional method that gives users
#                more control when displaying output.

animal = "cow"
item = "moon"

#print("The "+animal+" jumped over the "+item".") #previous method to write line.

#another way...
#print("The {} jumped over the {}.".format(item,animal)) #replaces {} with desired variable value.
#print("The {1} jumped over the {0}.".format(animal,item)) #positional argument.
#print("The {animal} jumped over the {animal}.".format(animal="cow",item="moon")) #keyword argument.

#another way...
text = "The {} jumped over the {}."
print(text.format(animal,item)) #easiest way.

#add padding to a string when we display it

name = ("Bro")

print("Hello, my name is {}.".format(name))
print("Hello, my name is {:10}.".format(name)) #adds 10 spaces in after the name.
print("Hello, my name is {:<10}.".format(name)) #left align.
print("Hello, my name is {:>10}.".format(name)) #right align.
print("Hello, my name is {:^10}.".format(name)) #center align.

#how can we format some numbers?

number = 1000
#display the first 2 digits after decimal:
print("The number pi is {:.2f}.".format(number)) #f=floating point numbers
print("The number is {:,}.".format(number)) #add a comma in 1,000
print("The number is {:b}.".format(number)) #displayed as binary
print("The number is {:o}.".format(number)) #displayed as octal
print("The number is {:x}.".format(number)) #lower case x = lower case
print("The number is {:X}.".format(number)) #upper case x = upper case
print("The number is {:e}.".format(number)) #display as scientific notation




