from flask import Flask
from logic import square_of_number_plus_nine


# Create Flask's `app` object
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

# Create Flask's `app` object
app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder="templates",
    static_folder="static"
)

@app.route("/")
def hello():
    value = square_of_number_plus_nine(5)
    return value