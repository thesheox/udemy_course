class Duck:
    def walk(self):
        print("duck is walking")

    def talk(self):
        print("duck is talking")


class Chicken:
    def walk(self):
        print("chicken is walking")

    def talk(self):
        print("chicken is talking")


class Person:

    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("you caught the duck")

duck1 = Duck()
chicken1 = Chicken()
person1 = Person()

person1.catch(duck1)