# dictionary = a changeable, unordered collection of unique key-value pairs.
# they are fast because they use hashing, allows us to access a value quickly.

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"} #creates a dictionary.

# print(capitals["Russia"]) #prints the value associated with the key 'Russia'.
# print(capitals.get("Germany")) #non-existent key will display none is get is used.
print(capitals.keys()) #will print only keys and not values.
print(capitals.values()) #will print only values and not keys.
print(capitals.items()) #will print keys and values in the dictionary.



capitals.update({"Germany": "Berlin"}) #adds to capitals dictionary.
capitals.update({"USA": "Las Vegas"}) #changes key and value.


capitals.pop("China") #removes item from dictionary.
capitals.clear() #clears dictionary.

for key,value in capitals.items(): #will print dictionary a bit cleaner.
    print(key, value)