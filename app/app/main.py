from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    # 開発中のみ利用
    app.run(host="0.0.0.0", port=8080, debug=True)

