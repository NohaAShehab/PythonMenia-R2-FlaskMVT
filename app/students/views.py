from app.models import Student,db
from flask import  render_template, redirect, url_for, request
from app.students.forms import StudentForm

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

def validateInputs(requestdict: dict):
    errors = {}
    if not requestdict["name"]:
        errors["name"] = 'name required'

    ## check email exists before
    student = Student.query.filter_by(email=requestdict['email']).first()
    if student:
        errors["email"] = 'Email already exists'

    return errors




#### create
@students_blueprint.route('/create',endpoint='create', methods=['GET','POST'])
def createStudent():
    if request.method == 'GET':
        return render_template('students/create.html')
    elif request.method == 'POST':
        print(request.form)  # use request.form
        requestdata = dict(request.form)
        print(requestdata)
        if not 'accepted' in requestdata:
            requestdata['accepted']=False
        else:
            requestdata['accepted'] = True


        request_errors = validateInputs(requestdata)
        if request_errors:
            return render_template('students/create.html',errors=request_errors)
        else:
            student = Student(**requestdata)
            db.session.add(student)
            db.session.commit()

            return redirect(url_for('students.students_index'))





@students_blueprint.route('/forms/create',endpoint='forms_create', methods=['GET','POST'])
def createStudentUsingForm():
    form  = StudentForm()
    if request.method == 'GET':
        return render_template('students/createform.html', form=form)
    elif request.method == 'POST':
        print(request.form)  # use request.form
        requestdata = dict(request.form)
        print(requestdata)
        if not 'accepted' in requestdata:
            requestdata['accepted']=False
        else:
            requestdata['accepted'] = True


        request_errors = validateInputs(requestdata)
        if request_errors:
            return render_template('students/createform.html',errors=request_errors,form=form )
        else:
            del requestdata['csrf_token']
            student = Student(**requestdata)
            db.session.add(student)
            db.session.commit()

            return redirect(url_for('students.students_index'))

