class Animal:
    alive=True
    def eat(self):
        print("this animal is eating")
    def sleep(self):
        print("rhis animal is sleeping")

class Rabbit(Animal):
    pass

class Fish(Animal):
    pass

class Hawk(Animal):
    pass


rabbit=Rabbit()
fish=Fish()
hawk=Hawk()

rabbit.eat()
fish.eat()
hawk.eat()