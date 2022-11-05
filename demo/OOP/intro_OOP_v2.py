
## This is  a class, this doesn't exist in the memory yet. But this is a blueprint for creating objects
class Animal:
    name = ""
    species = ""
    color = ""
    def __init__(self, name, species, color = "red"):
        self.name = name
        self.species = species
        self.color = color

    def speak(self):
        ...
    
    def whoami(self):
        print(f"my name is {self.name} and I am a {self.color} {self.species}")


animal = Animal("Ghoda", "Horse")
animal.whoami()

animal2 = Animal("Kutta", "Dog", "black")
animal2.whoami()

print("Animal 1 type",type(animal), "::: Animal 2 type",type(animal2), "::: equality", type(animal) == type(animal2))