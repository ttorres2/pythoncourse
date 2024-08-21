print("I love pizza")
print("It's really good")
#Simple print program.

#string data type
first_name = "Tom" #string variable
last_name = "Torres" #another variable
full_name = first_name + " " +last_name #full_name variable will print with space.
print ("Hello "+first_name) #prints the variable with string, no quotes on variable.
print (type(first_name)) #checks the datatype and prints if for you, see output below.
print ("Hello "+full_name)

#int data type
age = 21 #no quotes since it is not a string data type
age = age+1 #self explanatory
print (age) #self explanatory
print (type(age))#prints data type of age variable
print ("Your age is: "+str(age))#To print two different data types

#float data type
height = 250.5 #float (with decimal)
print(height)
print (type(height))
print("Your height is: "+str(height)+" cm.")#converts height to string concatentation

#boolean data type
human = False
print(human)
print(type(human))
print("Are you a human: "+str(human))

#multiple assignment of variables
name = "Tom"
age = 21
attractive = True

print(name)
print(age)
print(attractive)

name, age, attractive = "Tom", 21, True #assign multiple variables in one line of code
print(name, age, attractive)

Spongebob = 30
Patrick = 30
Sandy = 30
Squidward = 30
#if all variables equal the same value, syntax changes a little
Spongebob = Patrick = Sandy = Squidward = 30
