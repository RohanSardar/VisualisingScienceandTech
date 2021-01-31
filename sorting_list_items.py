# Program to sort the items of a list in ascending & descending
# order

# First create two lists, one for numbers and one for strings
mynum = [45, 65, 32, 2, 8, 1]
mystring = ["Banana", "Watermelon", "Apple", "Coconut"]

# Now, let us print these two lists in ascending order
mynum.sort()
mystring.sort()

print (mynum)
print (mystring)

# Now, let us print those two lists in descending order
mynum.sort(reverse=True)
mystring.sort(reverse=True)
#(reverse=True) is used to write the items in descending order

print (mynum)
print (mystring)
