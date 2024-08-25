# def outer_function():
#     print("im outer")
#
#     def nested_function():
#         print("im inner")
#     return nested_function
#
#
# inner_function=outer_function()
# inner_function()
#

import time
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
        function()
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello World!")

@delay_decorator
def say_goodbye():
    print("Good Bye!")

def say_greeting():
    print("Greetings!")


say_hello()