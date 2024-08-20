#String slicing is when you create a substring by extracting elements from another string.
#You can either use the indexing[] operator or slice() function.
#There are three optional arguments:  [start:stop:step].

name = "Tom Torres"

#indexing operator

#create a substring based off a sliced portion of the string above, step is how much you are increasing index each time.
first_name = name[0:3] #:3 would be everything up to and including position 3.
last_name = name[4:10] #4: would be everything including and after position 4.
funky_name = name[::2] #skips over 2 positions each time until the end of the string.
reversed_name = name [::-1] #reverses the string.

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

#slice function

website1 = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7,-4) #starts at position 7 and ends -4 from the right since most website name lengths vary.
print(website1[slice])
print(website2[slice])
