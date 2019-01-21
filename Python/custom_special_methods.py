from random import choice as c

class Animal:
    def __len__(self):
        return 50

    def speak(self):
        raise NotImplementedError("this isn't implemented")

class Dog(Animal):
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def __repr__(self):
        return f"{self.name} is a {self.age} year old {self.species}"

    def __add__(self, other):
        z = ["Stella", "Fritz", "Jumbo", "Zoom", "Staci"]
        if isinstance(other, Dog):
            return Dog(c(z), self.species, 0)
        else:
            return "You can't do that!"


d=Dog("Boris", "Cockapoo", 4)
j = Dog("Ovis", "Maltese", 2)
# print(d.speak())
k = d + j
print(k)
