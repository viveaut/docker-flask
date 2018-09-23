from app.app.main import app

@app.route("/")
def hello():

    return "Oh, Hello World"


@app.route("/login")
def login():
    return "login"
