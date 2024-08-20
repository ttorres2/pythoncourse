# set = a collection which is unordered, unindexed. No duplicate values.
# a set is faster than a list.

utensils = {"fork","spoon","knife","knife","knife"} #only displays items not amount of times they are listed.
dishes = {"bowl","plate","cup","knife"}
#dinner_table = utensils.union(dishes) #has elements from both sets.

#utensils.add("napkin") #adds napkin from set.
#utensils.remove("fork") #removes fork from set.
#utensils.clear() #clears all elements within the set.
#dishes.update(utensils) #adds two sets together, appends dishes to utensils set.

# for x in dinner_table: #)when printed, the values will not always display in order when surrounded by {}.
#    print(x)

#check to see what utensils has that dishes doesn't or vice versa.
#print(utensils.difference(dishes))

print(utensils.intersection(dishes)) #will return what elements they have in common.

