

### api ---> flask_restful
from flask_restful import Resource, Api, marshal_with, abort
from app.models import  Student
from app.students.api.serilizers import student_serilizer
from  app.students.api.parser import  student_parser
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}




class StudentList(Resource):
    @marshal_with(student_serilizer)
    def get(self):
        students=  Student.get_all_students()
        return students

    @marshal_with(student_serilizer)
    def post(self):
        ## use student parser to get object from request
        students_args = student_parser.parse_args()  # return args in form of dict
        student = Student.create_student(students_args)
        return  student, 201


class StudentOperation(Resource):
    @marshal_with(student_serilizer)
    def get(self, id):
        student = Student.get_specific_student(id)
        if student:
            return student, 200

        return abort(404, message="Student not found.")

    @marshal_with(student_serilizer)
    def put(self, id):
        student = Student.get_specific_student(id)
        if student:
            student_args = student_parser.parse_args()
            student.update_student(student_args)
            return student, 200

        return 'Student not found , please reload the page', 205

    def delete(self, id):
        student = Student.get_specific_student(id)
        if student:
            student.delete_object()
            return 'Student deleted', 204

        return 'Student not found , please reload the page', 205