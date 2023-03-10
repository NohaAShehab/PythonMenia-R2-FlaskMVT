from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from app.models import Student
from wtforms.widgets import CheckboxInput

from wtforms import BooleanField

class StudentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email')
    age = IntegerField('Age')
    accepted = BooleanField('Accepted')



    def validate_email(self, field):
        student = Student.query.filter_by(email=self.email)
        if student:
            return ValidationError["email already exists"]
