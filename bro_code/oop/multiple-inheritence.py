class Prey:
    def flee(self):
        print("this animal flees")


class Predator:
    def hunt(self):
        print("this animal hunts")


class Fish(Prey, Predator):
    pass

fish=Fish()
fish.flee()
fish.hunt()