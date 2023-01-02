from flask import Flask
from .site.routes import site
from .authentication.routes import auth
from .api.routes import api
from .models import db as root_db
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager
from .models import User
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(site)
app.register_blueprint(auth)
lm = LoginManager()
app.config.from_object(Config)

root_db.init_app(app)
migrate = Migrate(app, root_db)
lm.init_app(app)
@lm.user_loader
def load_User(user_id):
    return User.query.get(user_id)

from . import models
