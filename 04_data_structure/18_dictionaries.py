

# we can create dictionary like this
user = {
    "name": "Manoj",
    "age": 27,
    "city": "Mysuru"
}

# we have another method like this
person1 = dict(name="Manoj", age=29)

print("user data :", user)
print("person1 :", person1)


# we can access the value based on key like this
print(user["name"])
# if key is not there if try to access like that we will get the error
# print(user["s"])

# we can overcome that error like this
if "s" in user:
    print(user["s"])


# we have another technique to access the value from dictionary
print(user.get("age"))

# In this method if key is not there it will give "None"
print(user.get("sad"))

# in this method we can pass the second variable as default
print(user.get("aaa", "Doesn't have"))


print("*************looping test************")
# we can loop the dictionary like this
for key, value in user.items():
    print(key, value)
