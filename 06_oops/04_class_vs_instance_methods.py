# A class method is a method that belongs to class rather than the instance. 
# It is defined using the @classmethod decorator and takes "cls" as its first parameter.
# It is often used as a factory method to create objects with predefined values.


class Point:

    # constructor method
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    @classmethod
    def zero(cls):
        return cls(0,0)

    def draw(self):
        print(f"Point ({self.x} {self.y})")
        
# creating an object
point1 = Point(0,0)
point1.draw()

# we can create same object using class method like this 
point2 = Point.zero()
point2.draw()
