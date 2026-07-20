class Animal:
    def make_sound(self):
        print("Some Sound")
    
class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")
    
class Cow(Animal):
    def make_sound(self):
        print("Moo")

animals = [Dog(),Cat(),Cow()]

for animal in animals:
    animal.make_sound()