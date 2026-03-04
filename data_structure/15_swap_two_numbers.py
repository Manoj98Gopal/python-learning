
# swap two numbers

x = 10
y = 20

print(f"x={x}, y={y}")

print("normal way swapping two numbers")

z = x
x = y
y = z

print(f"x={x}, y={y}")


print("Second experiment")

a = 30
b = 20

# we can achieve this without third variable

print(f"a={a}, b={b}")

print("After swapping :")

a, b = b, a
print(f"a={a}, b={b}")

# what happens python treats that as a tuple and they are unpacking the tuple and assigning
