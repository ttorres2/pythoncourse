#stringmethods

name = "bro code"
print(len(name)) #returns how long the string is.
print(name.find("B")) #finds position of B in Bro Code, which returns 0.
print(name.capitalize()) #capitalizes name.
print(name.upper()) #prints name in all caps.
print(name.lower()) #prints in all lower case.
print(name.isdigit()) #prints whether or not name is a digit.
print(name.isalpha()) #are these alphabetical characters?
print(name.count("o")) #count how many characters within string are a certain value.
print(name.replace("o","a")) #replaces o with a in string.
print(name*3) #prints name variable 3 times.

#type casting = convert a data type of a value to another data type.

x=1 #int
y=2.0 #float
z="3" #str

x = float(x) #converts int to a float for x variable
y = str(y)
z = int(z)

print(x)
print(int(y)) #changes datatype of y variable to an integer
print(z*3) #prints z variable 3 times

print ("X is "+str(x)) #display x and y variables as strings using type casting.
print("Y is "+str(y))
print (z*3)