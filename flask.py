from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome in Mukesh-Flask Application"


if __name__ == "__main__":
    app.run(debug=True)