from flask import render_template
from app.models import Department
from app.departments import  departments_blueprint

@departments_blueprint.route('/')
def department_index():
    departments = Department.get_all_departments()
    return render_template('departments/index.html',departments=departments )
