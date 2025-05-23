from flask import Flask

from .events import Socketio
from .routes import main

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "secret"

    app.register_blueprint(main)

    Socketio.init_app(app)

    return app 
