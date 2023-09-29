from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def calculator_index():
    return render_template("calculator.html")


@app.route('/calculate', methods=['POST'])
def calculate():
    num_one = request.form['num_one']
    num_two = request.form['num_two']
    operation = request.form['operation']

    if operation == 'add':
        result = {
            'operation': f"{float(num_one)} + {float(num_two)}",
            'result': float(num_one) + float(num_two)
        }
        return render_template("calculator.html", result=result)
    elif operation == 'subtract':
        result = {
            'operation': f"{float(num_one)} - {float(num_two)}",
            'result': float(num_one) - float(num_two)
        }
        return render_template("calculator.html", result=result)
    elif operation == 'multiply':
        result = {
            'operation': f"{float(num_one)} * {float(num_two)}",
            'result': float(num_one) * float(num_two)
        }
        return render_template("calculator.html", result=result)
    elif operation == 'divide':
        result = {
            'operation': f"{float(num_one)} / {float(num_two)}",
            'result': float(num_one) / float(num_two)
        }
        return render_template("calculator.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)
