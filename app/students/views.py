from app.models import Student
from flask import  render_template, redirect, url_for

# def testfunction():
#     return '<h1> Students Index </h1>'
#
#
# def students_index():
#     students = Student.get_all_students()
#     return render_template('students/index.html', students=students)
#
#
#
# def student_info(id):
#     student = Student.query.get_or_404(id)
#     return render_template('students/show.html', student=student)
#
#
#
# def student_delete(id):
#     student = Student.query.get_or_404(id)
#     res =student.delete_object()
#     if res :
#         return redirect(url_for("students_index"))
#

from app.students import  students_blueprint

@students_blueprint.route('test')
def testfunction():
    return '<h1> Students Index </h1>'


@students_blueprint.route('')
def students_index():
    students = Student.get_all_students()
    return render_template('students/index.html', students=students)


@students_blueprint.route('/<int:id>')
def student_info(id):
    student = Student.query.get_or_404(id)
    return render_template('students/show.html', student=student)


@students_blueprint.route('/<int:id>/delete', endpoint='delete')
def student_delete(id):
    student = Student.query.get_or_404(id)
    res =student.delete_object()
    if res :
        return redirect(url_for("students.students_index"))

