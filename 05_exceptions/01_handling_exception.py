

try:
    age = int(input("age :"))
except ValueError as error:
    print("You entered wrong age")
    print(error)
    print(type(error))
else:
    print("You entered age is :", age)



