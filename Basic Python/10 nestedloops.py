# nested loops = The 'inner loop' will finish all of its iterations before
#                finishing one iteration of the 'outer loop'.

#create a program to create a rectangle

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="") #prevents cursor from moving to the next line (end)
    print()

