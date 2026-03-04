numbers = list(range(5))
alpha = ["a", "b", "c"]

print("list of numbers :", numbers)

# in javascript we have spread operator similarly in python  unpack operator is there
# javascript if we want  merge two list   [...numbers, ...alpha]

combined = [*numbers, *alpha]
print("combined :", combined)


# we can spread the object to by using this symbol(**)

obj1 = {
    "name": "Manu Man",
    "age": 27
}

obj2 = {
    "name": "Manoj G",
    "city": "Mysore"
}

combinedObj = {**obj1, **obj2}
print("combined object :", combinedObj)
