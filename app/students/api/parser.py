from flask_restful import  reqparse

student_parser = reqparse.RequestParser()

student_parser.add_argument('name', type=str,help='Student name is required', required=True )
student_parser.add_argument('email', type=str,help='Student Email' )
student_parser.add_argument('age', type=int ,help='Student age' )
student_parser.add_argument('dept_id', type=int ,help='Student department' )
student_parser.add_argument('accepted', type=bool ,help='Student accepted' )


