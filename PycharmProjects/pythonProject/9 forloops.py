import time
#program that counts down by 10 with exact timing.
for seconds in range(10,0,-1):
    print (seconds)
    time.sleep(1)
print("Happy New Year!")

#for loop = a statement that will execute it's block of code
#           a limited amount of times.
#
#           while look = unlimited
#           for loop = limited

for i in range(10): #execute for loop 10 times
    print(i) #block of code it will execute by printing from 0 ten times to 9

for i in range(50,100+1,2):
    print(i) #prints 50 to 100

for i in "Tom Torres":
    print(i) #prints each letter in the string
