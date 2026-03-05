# Example of using properties in Python

class Product:

    def __init__(self, price):
        # When object is created, the setter method is called
        # because we are assigning value to self.price
        self.price = price

    # Property decorator
    # This method allows us to access the price like an attribute
    # Example: watch.price
    @property
    def price(self):
        return self.__price

    # Setter method for the property
    # This method is automatically called when we assign a value
    # Example: watch.price = 2000
    @price.setter
    def price(self, price):

        # Validation logic
        if price < 0:
            raise ValueError("Negative number is not allowed")

        # Private variable
        self.__price = price


# Creating object
watch = Product(1500)

# Accessing price using property
print(watch.price)

try:
    # Trying to assign negative price
    watch.price = -500
except Exception as e:
    print(e)

# Price remains unchanged
print(watch.price)