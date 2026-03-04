
from sys import getsizeof

values = [x*2 for x in range(10)]

print("list of values are :")

for x in values:
    print(x)


print("generative object iteration")

# see generator object
values = (x*2 for x in range(10))

for x in values:
    print(x)


# we use this generative object when we handle large amount of data
# advantages is it takes less memory  example likes this
# it doesn't have len function, if we try we will get error 

list = [x*3 for x in range(100000)]
print("list size :", getsizeof(list))


generative_object = (x*3 for x in range(100000))
print("generative object :", generative_object)
print("generative object  size :", getsizeof(generative_object))
