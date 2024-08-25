from flask import Flask

app = Flask(__name__)
# print(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper
@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return "Hello, World!"


@app.route("/bye")
def good_bye():
    return ('<h1 style="text-align: center"> hi shayan</h1>'
            '<p> this is a paragragh</p>'
            '<img src="https://www.mediastorehouse.com.au/p/617/grey-tabby-cat-felis-silvestris-catus-9457549.jpg.webp"width=1000>')

# @app.route("<name>")
# def greet(name):
#     return f"Hello, {name}!"


@app.route("/user/<name>/<int:number>")
def greet(name,number):
    return f'Hello, {name}, you are {number}!'




if __name__=="__main__":
    app.run(debug=True)