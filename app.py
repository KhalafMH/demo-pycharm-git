from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello")
def hello():
    return "Hello"


@app.route("/hello", methods=['POST'])
def hello_name():
    name = request.form['name']
    return render_template("hello.html", data={"name": name})


if __name__ == '__main__':
    Flask.run(app)
