def calculate(n,**kwargs):
    n+=kwargs["add"]
    n+=kwargs["mul"]

    print(n)

calculate(2,add=3,sub=5,mul=6)


class Car:
    def __init__(self,**kw):
        self.make=kw.get("make")
        self.model=kw.get("model")

my_car=Car()