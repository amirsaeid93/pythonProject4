from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, this is my Flask app!'

@app.route('/alkuluku/<luku>')
def onko_alkuluku(luku):
    luku = int(luku)
    if luku <= 1:
        response = {"Number":luku, "isPrime": False}
        return jsonify(response)

    for jaollinen in range(2, int(luku ** 0.5) + 1):
        if luku % jaollinen == 0:
            response = {"Number":luku, "isPrime": False}
            return jsonify(response)

    return jsonify({"Number":luku, "isPrime": True})

if __name__ == '__main__':
    app.run(debug=True)