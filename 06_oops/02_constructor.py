# A Constructor is a special method in a class that is automatically called when an object is created.
# it is mainly used to initialize the object attributes


class Point:

    # constructor method
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x} {self.y})")


# creating object
point = Point(2, 3)

print(point.x)
point.draw()
