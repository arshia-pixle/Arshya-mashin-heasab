from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    try:
        a = float(data["a"])
        b = float(data["b"])
        op = data["op"]

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                return jsonify({"error": "Division by zero!"})
            result = a / b
        else:
            return jsonify({"error": "Invalid operation"})

        return jsonify({"result": result})

    except (ValueError, TypeError, KeyError):
        return jsonify({"error": "Invalid input"})

if __name__ == "__main__":
    app.run(debug=True)