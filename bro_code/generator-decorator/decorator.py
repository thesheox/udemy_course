# def func():
#     return 1
#
# def hello(name="Jose"):
#     print("the hello function has been executed")
#
#     def greet():
#         return "\t this is the greet function inside hello function"
#
#     def welcome():
#         return "\t this is the welcome function inside hello function"
#
#     print("returning function")
#     if name== "Jose":
#         return greet()
#     else:
#         return welcome()
#
# func=hello
# print(func())
#
#
#
# def cool():
#
#     def super_cool():
#         return "im so cool"
#
#     return super_cool()
#
#
# s_func=cool
# print(s_func())
#
import time


#
# def hello():
#     return "hi shayan"
#
# def other(some_func):
#     print("other codes run here")
#     print(some_func)
#
# other(hello())



def new_decorator(func):
    def wrapper():
        t1=time.time()
        func()
        t2=time.time()
        print(f"{func.__name__} rai in {t2-t1} seconds")
    return wrapper


def func_need_decorator():
    print(" i want to be decorated")


# dec_func=new_decorator(func_need_decorator)
# dec_func()

# @new_decorator
# def do_this():
#    time.sleep(1.3)
#
# @new_decorator
# def do_that():
#    time.sleep(4)
#
# do_this()
# do_that()
#


def add_sprinkle(func):
    def wrapper(*args,**kwargs):
        print("sprinkle added")
        func(*args,**kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args,**kwargs):
        print("fudge added")
        func(*args,**kwargs)
    return wrapper

@add_sprinkle
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream")

get_ice_cream("vanilla")