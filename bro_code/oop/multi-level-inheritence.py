class Organism:
    alive=True

class Animal(Organism):
    def eat(self):
        print("the animal is eating")
class Dog(Animal):
    def bark(self):
        print("the dog is barking")

dog=Dog()
print(dog.alive)
print(dog.eat())
print(dog.bark())