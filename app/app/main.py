from . import app

if __name__ == '__main__':
    # 開発中のみ利用
    app.run(host="0.0.0.0", port=8080, debug=True)

@app.route("/")
def hello():

    return "Oh, Hello World"


@app.route("/login")
def login():
    return "login"
