
def increment(number, by, name):
    return f"{number + by}, {name}"


# These are the keyword arguments
result = increment(name="manoj", number=10, by=30)

print("result is :", result)


# Default arguments
def increment_by_one(number, by=1):
    print(number + by)


increment_by_one(20)
