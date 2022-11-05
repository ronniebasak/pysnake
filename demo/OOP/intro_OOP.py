
## This is  a class, this doesn't exist in the memory yet. But this is a blueprint for creating objects
class Animal:
    name = ""
    species = ""
    color = ""
    def __init__(self):
        ...

    def speak(self):
        ...
    
    def whoami(self):
        print(f"my name is {self.name} and I am a {self.species}")


animal = Animal()
animal.name = "Ghoda"
animal.species = "Horse"

animal.whoami()