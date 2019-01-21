class Animal:
    def speak(self):
        raise NotImplementedError("this isn't implemented")

class Dog(Animal):
    def speak(self):
        return "wuf"


d=Dog()
print(d.speak())
