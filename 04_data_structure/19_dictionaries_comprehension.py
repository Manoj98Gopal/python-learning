# create list using normal method
list = []

for x in range(5):
    list.append(x)

print("list created with normal method :",list)

# using array comprehension method
list1 = [x for x in range(5)]
print("list created with comprehension method :",list1)


# we can create  sets too
set = {x for x in range(5)}
print("set values :",set)


# mainly difference between sets and dictionary, In the dictionary key, values pair with separated with commas
dic = {x:x*2 for x in range(5)}
print("dictionary :",dic)


# we can create tuples too 
tuple = (x*2 for x in range(10))
print("tuples :",tuple) #<generator object <genexpr> at 0x799702e44510>  this is the next topic called generator expressions