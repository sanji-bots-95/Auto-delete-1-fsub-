from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '@Straw_Hat_Bots'


if __name__ == "__main__":
    app.run()