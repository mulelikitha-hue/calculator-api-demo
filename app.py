from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Calculator API Running"

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return {"result": a + b}

if __name__ == "__main__":
    app.run(debug=True)
