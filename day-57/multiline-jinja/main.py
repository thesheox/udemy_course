import requests
from flask import Flask, render_template


app = Flask( __name__)

@app.route('/blog')
def blog():
    blog_url='https://api.npoint.io/c790b4d5cab58020d391'
    requests.get(blog_url)
    all_posts=requests.json()
    return render_template("index.html",posts=all_posts)

if __name__ == '__main__':
    app.run(debug=True)
