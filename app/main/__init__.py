from flask import Flask
from .model.example_model import db
from .controller.example_controller import example_blueprint

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    db.init_app(app)
    app.register_blueprint(example_blueprint, url_prefix='/api')
    return app