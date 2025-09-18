from flask import Flask

app = Flask(__name__)

# Index view
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print string view
@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return text

# Count view
@app.route('/count/<int:num>')
def count(num):
    result = ""
    for i in range(num):
        result += f"{i}\n"
    return result

# Math view
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    elif operation == '*':
        answer = num1 * num2
    elif operation == 'div':
        answer = num1 / num2
    elif operation == '%':
        answer = num1 % num2
    else:
        return "Invalid operation!"
    return str(answer)

if __name__ == '__main__':
    app.run(debug=True)
