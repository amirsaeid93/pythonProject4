from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def hello():
    return ('Hi,'
            'and welcome to to 2 number sum page.'
            'Please enter your numbers after the url adress in this form = /summa/number1/number2')


@app.route('/summa/<luku1>/<luku2>')
def summa(luku1, luku2):
    summa = float(luku1) + float(luku2)
    Response = {

        'luku1': luku1,
        'luku2': luku2,
        'summa': summa
    }
    return Response
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)