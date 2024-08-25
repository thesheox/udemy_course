from flask import Flask

app = Flask(__name__)
# print(__name__)
@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/bye")
def good_bye():
    return "bye"






if __name__=="__main__":
    app.run()