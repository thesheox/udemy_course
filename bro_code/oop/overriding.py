class Animal:
    def eat(self):
        print("this animal is Eating...")


class Cat(Animal):
    def eat(self):
        print("this cat is Eating...")


cat=Cat()
cat.eat()