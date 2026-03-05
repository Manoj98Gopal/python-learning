# Multiple inheritance is an OOP concept where a child class inherits properties and methods from more than one parent class


class Flyable:
    
    def fly(self):
        print("Can fly")
        
        
class Swimmable:
    
    def swim(self):
        print("Can swim")
        
        
class Duck(Flyable,Swimmable):
    
    def walk(self):
        print("Can walk")
        
        
        
duck1 = Duck()

duck1.fly()
duck1.swim()
duck1.walk()