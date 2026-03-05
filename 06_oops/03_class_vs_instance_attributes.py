# class attribute is sharing to all objects, if change the value of class attribute it will reflect to all object.
# Instance attribute is not sharing, it belongs to created object, if you change also it won't effect to another object


class Point:

    # class attribute
    default_color = "red"

    # constructor method
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x} {self.y})")
        

Point.default_color = "Yellow"


# creating object
point = Point(2, 3)
# instance attribute
point.z = 30

# creating another object
another_point = Point(5,6)
another_point.z = 45


point.draw()
print("point default color :",point.default_color)
print("point z value :",point.z)
point.z = 100
print("point after changing the z value :",point.z)

print("*************Another object*************")
another_point.draw()
print("another_point default color :",another_point.default_color)
print("another_point z value :",another_point.z)
