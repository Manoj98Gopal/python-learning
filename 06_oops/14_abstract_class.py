# An abstract class is a class than cannot directly create an object and used as a blueprint for another classes.
# It can contain abstract methods that must be implemented by child classes.
# In python, abstract classes are created using ABC module and the @abstractmethod decorator


from abc import ABC, abstractmethod


# Custom exception for invalid stream operations
class InvalidOperationError(Exception):
    pass


# Abstract Base Class
class Stream(ABC):

    def __init__(self):
        # This attribute keeps track of stream state
        self.opened = False

    # Method to open the stream
    def open(self):
        if self.opened:
            # Prevent opening an already opened stream
            raise InvalidOperationError("Stream is already opened!")
        self.opened = True

    # Method to close the stream
    def close(self):
        if not self.opened:
            # Prevent closing an already closed stream
            raise InvalidOperationError("Stream is already closed!")
        self.opened = False

    # Abstract method
    # Child classes MUST implement this method
    @abstractmethod
    def read(self):
        pass


# Concrete class for reading from files
class FileStream(Stream):

    def read(self):
        print("file is reading")


# Concrete class for reading from network
class NetworkStream(Stream):

    def read(self):
        print("network is reading")


# Concrete class for reading from memory
class MemoryStream(Stream):

    def read(self):
        print("Reading data from memory")


# Creating object of child class
memory = MemoryStream()

# Calling implemented method
memory.read()
