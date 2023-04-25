from flask import Flask
import random

application = Flask(__name__)

constant = [1, 2, 3, 4, 5]


@application.route("/")
def show_items():
    return f'<h3>This is a list of items: {constant}</h3>'


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8000, debug=True)
