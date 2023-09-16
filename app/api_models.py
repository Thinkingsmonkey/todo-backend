from flask_restx import fields
from .extensions import api

reset_input_model = api.model("ResetInput", {
    "email": fields.String,
    "password": fields.String
})
reset_output_model = api.model("ResetOutput", {
    "message": fields.String,
})


member_output_model = api.model("MembersOutput", {
    "id": fields.Integer,
    "username": fields.String
})
member_input_model = api.model("MembersInput", {
    "username": fields.String,
    "password": fields.String,
    "email": fields.String
})


member_login_model = api.model("MembersLogin", {
    "username": fields.String,
    "password": fields.String
})


task_model = api.model("Task", {
    "id": fields.Integer(required=False),
    "member_id": fields.Integer,
    "title": fields.String(required=True),
    "priority": fields.String(required=False),
    "state": fields.String(required=False),
    "start": fields.DateTime(required=False),
    "deadline": fields.DateTime(required=False),
    "description": fields.String(required=False)
})
task_update_model = api.model("TaskUpdate", {
    "id": fields.Integer,
    "member_id": fields.Integer,
    "title": fields.String,
    "priority": fields.String(required=False),
    "state": fields.String(required=False),
    "start": fields.DateTime(required=False),
    "deadline": fields.DateTime(required=False),
    "description": fields.String(required=False)
})
