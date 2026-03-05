# Magic methods are special methods in python that start and end with double underscores.
# They allow us to define how object should behave with builtin operations.


class Point:

    # Constructor method (magic method)
    # Automatically called when an object is created
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Instance method
    # Used to display the point coordinates
    def draw(self):
        print(f"Point ({self.x} {self.y})")

    # Magic method
    # __str__() controls what should be displayed when we print an object
    # It returns a readable string representation of the object
    def __str__(self):
        return f"Point ({self.x} {self.y})"


# Creating an object
point = Point(2, 4)

# If __str__ is not defined, Python prints object memory address
# Example: <__main__.Point object at 0x000001...>

# Since we defined __str__, Python prints the returned string instead
print(point)
