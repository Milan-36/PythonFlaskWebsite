from flask import Flask


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