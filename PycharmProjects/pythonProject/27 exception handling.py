# exception = events detected during detection that interrupt the flow of a program.

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e: #standard practice as e to display more of a reason.
    print(e)
    print("You cannot divide by zero.")
except ValueError as e:
    print(e)
    print("Enter only numbers, please.")
except Exception as e:
    print(e)
    print("Something went wrong :(")
else:
    print(result)
finally:
    print("This will always execute.")