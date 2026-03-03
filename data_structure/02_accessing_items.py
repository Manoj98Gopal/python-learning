letters = ["a", "b", "c", "d"]

print(letters)
print("before update", letters[1])
letters[1] = "B"
print("after update", letters)
print(letters[1:3])


numbers = list(range(20))

# print every second number
print(numbers[::2])

# revers the order
print(numbers[::-1])
