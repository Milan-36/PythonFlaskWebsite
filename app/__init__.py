from flask import Flask

def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False, template_folder="templates")
    app.config.from_object('config.Config')

    with app.app_context():
        # Include our Routes
        from Route import routes
        return app