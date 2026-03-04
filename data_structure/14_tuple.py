tuple = (1,2,3)

# python will consider this as also tuple
tuple1 = 3,4

# we can combine two tuples
print(tuple1 + tuple)

# we can access tuple like this 
print(tuple1[1])

# we can use slice method too
print(tuple[0:3]) #this will write another tuple


# we can unpack the tuple like this 
a,b,c = tuple

print("a =",a)


print(type(tuple))
print("tuple 1:",type(tuple1))