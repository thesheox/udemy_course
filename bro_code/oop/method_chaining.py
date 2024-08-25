class Car:
    def turn_on(self):
        print("Turning on")
        return self
    def drive(self):
        print("driving")
        return self

    def brake(self):
        print("breaking")
        return self
    def turn_off(self):
        print("turning off")
        return self


car=Car()

car.turn_on().drive().brake().turn_off()