from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("car is going")


class Motor(Vehicle):
    def go(self):
        print("motor is going")



motor=Motor()
motor.go()
car=Car()
car.go()




