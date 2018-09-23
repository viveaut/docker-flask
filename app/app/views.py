from app import app


@app.route("/")
def hello():
    print('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
    return "Oh, Hello World"


@app.route("/login")
def login():
    return "login"
