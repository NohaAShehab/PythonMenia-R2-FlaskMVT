
from flask_restful import fields
dept_serilizer= {
    'id': fields.Integer,
    'name': fields.String,
}



student_serilizer= {
    'id':fields.Integer,
    'name' :fields.String,
    'email': fields.String,
    'age':fields.Integer,
    'accepted':fields.Boolean,
    'dept_id': fields.Integer,
    'department': fields.Nested(dept_serilizer),
}

