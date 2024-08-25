def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text=func("hello")
    print(text)

hello(quiet)



def divisor(x):
    def divident(y):
        return y/x
    return divident


divide=divisor(2)
print(divide(3))



