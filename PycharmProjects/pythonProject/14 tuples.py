# tuple = a collection which is ordered and unchangeable used to group together related data.

student = ("Bro", 21, "male") #tuples use parenthesis instead of brackets.

print(student.count("Bro")) #count how many times a value appears in tuple.
print(student.index("male"))

for x in student: #print all values found in student tuple.
    print(x)

if "Bro" in student:
    print("Bro is here!")