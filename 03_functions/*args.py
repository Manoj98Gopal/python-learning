
# before parameter if we put "*" this symbol, it act as a tuple
def test(*numbers):
    print(numbers)


test(1, 2, 3, 4, 5, 6)


def multiply(*numbers):
    total = 1
    for num in numbers:
        total *= num

    return total


print(multiply(2, 3, 4, 5))


# if put "**" this symbol before parameter, it will give inside dictionary as arguments
def test1(**user):
    print(user)


test1(id=1, name="manoj", age=35)


def save_user(**user):
    print("full dictionary :", user)
    print("access name :", user["name"])


save_user(id=1, name="manoj", age=35)
