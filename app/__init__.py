

from flask import  Flask
from flask_migrate import Migrate
from  app.models import  db
from app.config import  projectConfig as AppConfig   # this dict
from app.models import Student,Department

from app.students.api.api_views import HelloWorld,StudentList, StudentOperation

from flask_restful import  Api

def create_app(config_name):
    app = Flask(__name__)
    current_config = AppConfig[config_name]  # class
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config # search in this class about class variable with this name
    app.config['SECRET_KEY'] = current_config.SECRET_KEY
    app.config.from_object(current_config)
    db.init_app(app)

    ## add migration
    migrate = Migrate(app, db, render_as_batch=True)

    ### add route
    # from app.students.views import testfunction,students_index, student_info, student_delete
    # from app.students.errors import page_not_found
    # from app.departments.views import department_index
    #
    #
    # app.add_url_rule('/test', view_func=testfunction)
    # app.register_error_handler(404, page_not_found)
    # app.add_url_rule('/students', view_func=students_index)
    # app.add_url_rule('/students/<id>', view_func=student_info)
    # app.add_url_rule('/students/<id>/delete', view_func=student_delete)

    #################### blueprints
    from app.departments import departments_blueprint
    from app.students import students_blueprint
    # app.add_url_rule('/departments', view_func=department_index, endpoint='departments_all')
    app.register_blueprint(departments_blueprint)
    app.register_blueprint(students_blueprint)


    ################## APIs
    ## app will use flask rest
    api = Api(app)
    ### add resource class
    api.add_resource(HelloWorld, '/api/hello')
    api.add_resource(StudentList, '/api/students')
    api.add_resource(StudentOperation, '/api/students/<int:id>')



    return  app



