# function = a block of code which is executed only when it is called.
# this is also called 'invoking' a function.

def hello(first_name, last_name, age): #def (define) followed by function name
    print("Hello "+first_name +last_name)
    print("You are " +str(age)+ " years old")
    print("Have a nice day!")

hello("Bro","Code", 21)