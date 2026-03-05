# Method overriding is an OOP concept where child class provide it's own implementation of a method that is already defined in the parent class.

class Animal:

    def __init__(self):
        # Parent class attribute
        self.age = 1

    # Parent class method
    def eat(self):
        print("animal is eating")


# Child class inheriting from Animal
class Mammal(Animal):

    def __init__(self):
        # Calling parent class constructor
        super().__init__()

        # Child class attribute
        self.weight = "10kg"

    # Method overriding
    # This method overrides the parent class eat() method
    def eat(self):
        print("mammal is eating")


# Creating object
m = Mammal()

# Calling overridden method
m.eat()

# Accessing inherited attribute
print(m.age)
