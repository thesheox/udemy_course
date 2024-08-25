from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/guess/<string:name>')
def home(name):
    response = requests.get(url=f"https://api.genderize.io?name={name}")
    response.raise_for_status()
    data = response.json()
    gender = data['gender']

    response = requests.get(url=f"https://api.agify.io?name={name}")
    response.raise_for_status()
    data = response.json()
    age = data['age']

    random_number = random.randint(1, 100)
    now_year = datetime.now().year

    return render_template("index.html", name=name, gender=gender, age=age, year=now_year, random_number=random_number)

if __name__ == '__main__':
    app.run(debug=True)
