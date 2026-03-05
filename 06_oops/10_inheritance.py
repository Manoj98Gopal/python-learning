# Inheritance allows one class (child class) to inherit
# properties and methods from another class (parent class)

class Animal:

    def __init__(self):
        # Instance attribute of parent class
        self.age = 1

    def eat(self):
        # Method defined in parent class
        print("eat")


# Mammal class inherits from Animal class
class Mammal(Animal):

    # Child class method
    def walk(self):
        print("walk")


# Fish class inherits from Animal class
class Fish(Animal):

    # Child class method
    def swim(self):
        print("swim")


# Creating objects
m = Mammal()
f = Fish()

# Accessing inherited attribute from Animal class
print(m.age)
print(f.age)

# Accessing child class methods
m.walk()
f.swim()

# Accessing parent class method
m.eat()
f.eat()


print(isinstance(m,Animal))
print(isinstance(m,object))
print(issubclass(Mammal,Animal))