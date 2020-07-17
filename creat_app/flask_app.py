from flask import  Flask

app = Flask('my app')


@app.route("/")
def index():
    return "<h1>WELCOME TO MY SITE</h1>"

@app.route("/images")
def images():
    return "images"

app.run()