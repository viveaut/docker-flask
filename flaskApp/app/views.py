from flaskApp import app


@app.route("/")
def hello():
    return "Oh, Hello World"
