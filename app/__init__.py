

from flask import  Flask
from  app.models import  db
from app.config import  projectConfig as AppConfig   # this dict


def create_app(config_name):
    app = Flask(__name__)
    current_config = AppConfig[config_name]  # class
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config # search in this class about class variable with this name

    app.config.from_object(current_config)
    db.init_app(app)

    ### add route
    from app.students.views import index
    app.add_url_rule('/students', view_func=index)

    return  app



