# Comparing objects using magic methods

class Point:

    # Constructor method (called automatically when object is created)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Instance method to display coordinates
    def draw(self):
        print(f"Point ({self.x} {self.y})")

    # Magic method for equality comparison (==)
    # It compares object attributes instead of memory addresses
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Magic method for greater-than comparison (>)

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


# Creating objects
point = Point(4, 4)
point1 = Point(2, 3)

# Because of __eq__ method, Python compares x and y values
print(point == point1)   # False

# This will give an error because __lt__ (less-than) is not defined
print(point < point1)
