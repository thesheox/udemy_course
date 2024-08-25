class Car:
    color=None


class Motor:
    color=None

def change_color(viechle,color):
    viechle.color=color


car_1=Car()
car_2=Car()
car_3=Car()

change_color(car_1,"red")
change_color(car_2,"blue")
change_color(car_3,"green")

print(car_1.color)
print(car_2.color)
print(car_3.color)



motor_1=Car()
motor_2=Car()
motor_3=Car()

change_color(motor_1,"red")
change_color(motor_2,"blue")
change_color(motor_3,"green")

print(motor_1.color)
print(motor_2.color)
print(motor_3.color)