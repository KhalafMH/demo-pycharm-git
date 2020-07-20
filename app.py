from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return \
        """
        <form method='post' action='http://localhost:5000/hello'>
            <input type='text' name='name' placeholder='Name'>
            <input type='submit'>
        </form>
        """


@app.route("/hello")
def hello():
    return "Hello"


@app.route("/hello", methods=['POST'])
def hello_name():
    name = request.form['name']
    return f"Hello {name}"


if __name__ == '__main__':
    Flask.run(app)
