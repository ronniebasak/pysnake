
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



## dog inherits animal
class Dog(Animal):
    def __init__(self, name, color="red"):
        super().__init__(name, "dog", color)

    def speak(self):
        print(f"Bark, Bark! from {self.name}")

## horse also inherits animal
class Horse(Animal):
    def __init__(self, name, color="red"):
        super().__init__(name, "horse", color)

    def speak(self):
        print(f"Neigh! Neigh!! from {self.name}")



animal1 = Dog("Johnny", "yellow")
animal2 = Horse("Alan", "purple")

animal1.whoami()
animal2.whoami()

animal1.speak()
animal2.speak()

print("Animal 1 type",type(animal1), "::: Animal 2 type",type(animal2), "::: equality", type(animal1) == type(animal2))

print()
print("is Animal1 Dog", isinstance(animal1, Dog))
print("is Animal1 Horse", isinstance(animal1, Horse))
print("is Animal1 Animal", isinstance(animal1, Animal))

print()
print("is Animal2 Dog", isinstance(animal2, Dog))
print("is Animal2 Horse", isinstance(animal2, Horse))
print("is Animal2 Animal", isinstance(animal2, Animal))