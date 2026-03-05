# A polymorphism is a OOP concept and poly means many and morphism means many forms
# A same name method behave differently depends on that object calls it.


class Dog:
    
    def speak(self):
        print("Dog barks")


class Cat:
    
    def speak(self):
        print("Cat meows")
        
        
class Cow:
    
    def speak(self):
        print("Cow moos")