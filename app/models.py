
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Department(db.Model):
    __tablename__= 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    ##### db.relationship("ModelName", -----)
    students = db.relationship('Student', backref='department', lazy=True)

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_all_departments(cls):
        return cls.query.all()



class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email= db.Column(db.String(100),unique=True, nullable=True)
    accepted = db.Column(db.Boolean, default=True)
    age = db.Column(db.Integer, default=10, nullable=True)
    ############################### db.foreignkey(table_name.id)
    dept_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable= True)


    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_all_students(cls):
        return cls.query.all()


    def delete_object(self):
        db.session.delete(self)
        db.session.commit()
        return True

    @classmethod
    def create_student(cls, student_data):
        student = cls(**student_data)
        db.session.add(student)
        db.session.commit()
        return student

    @classmethod
    def get_specific_student(cls, id):
        return cls.query.get(id)


    def update_student(self, updated_data):
        self.name = updated_data["name"]
        self.email = updated_data["email"]
        self.dept_id = updated_data["dept_id"]
        self.accepted = updated_data["accepted"]
        self.age =updated_data['age']
        db.session.add(self)
        db.session.commit()
        return True
