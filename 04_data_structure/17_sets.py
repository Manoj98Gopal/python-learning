
numbers = [1,2,3,4,4,3]

# using set function we can convert array into the sets
first = set(numbers)

# after converting the set duplicates will removed
print(first)

# we can add items into the set like this 
first.add(50)
print("after adding the item 50", first)

# we can remove items from the list
first.remove(50)
print("after removing the item 50", first)

# Now I am creating one more set
second = {2,4,1,10,11}


# unions of the sets
print(first | second)

# intersection of the sets
print(first & second)

# difference between two sets
print(first - second)

# spmatrix difference of two sets
print(first ^ second)