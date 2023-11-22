from flask import flask,

app = Flask(__name__)

@app.route('/')
def say_hello():
    return "Moi maailma"

@app.route('/')



if __name__ == '__main__':
    app.run
