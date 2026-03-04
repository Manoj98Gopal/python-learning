from array import array


num = [1,2,3,4] #list
numbers = array("i",[1,2,3,4,5,67,7,8])

print("list :",type(num))
print("array :", type(numbers))

# use array for large set of numbers  
# when we creating the array we should give  type code (means  inters, float, string...)

# we can do crud operation like list

print("array list :",numbers)

# adding the item into the array
numbers.append(100)
print("After adding the array :",numbers)

# adding the item specific index
numbers.insert(1,99)
print("After adding the array to specific index :",numbers)

# accessing the array by index
print("accessing by index :",numbers[1])

# we can update array using  index but same type
numbers[0] = 333

print("after updating the array", numbers)

# remove the item into the array
numbers.pop()
print("after removing the item into the array",numbers)

# remove a specific index item
numbers.pop(1)
print("after removing first index array :",numbers)

# remove based on value
numbers.remove(333)
print("after removing the 333 value :",numbers)

# remove using splice method
del numbers[1:4]
print("after removing the splice removing:",numbers)

# how to empty the array
numbers = []
print("assign empty array:",numbers)