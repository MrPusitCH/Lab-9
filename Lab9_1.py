from flask import Flask

app = Flask(__name__)

@app.route('/<opt>/<int:a>/<int:b>')
def calculate(opt, a, b):
    result = None
    if opt == 'add':
        result = a + b
    elif opt == 'sub':
        result = a - b
    elif opt == 'mul':
        result = a * b
    elif opt == 'div':
        if b != 0:
            result = a / b
        else:
            return "Error: Division by zero!"

    return f"The result of {a} {opt} {b} is {result}"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
