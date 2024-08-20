# nested function calls = function calls inside other function calls.
#                         Innermost function calls are resolved first.
#                         Returned value is used as argument for the next outer function.

num = input("Enter a whole positive number: ")
num = float(num) #converts to a floating point number
num = abs(num) #find absolute value
num = round(num) #round to nearest number
print(num)

print(round(abs(float(input("Enter a whole positive number: "))))) #consolidation of above code.

