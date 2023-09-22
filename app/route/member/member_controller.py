from flask_restx import Resource, Namespace
from flask_jwt_extended import create_access_token, set_access_cookies
from flask_jwt_extended import create_refresh_token, set_refresh_cookies
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_csrf_token
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from ...api_models import *
from ...models import generate_salt, Member
from flask import jsonify, abort

from .member_model import *

# 類似 blueprint 設一個 url_prefix = "/api" 的意思
member_ns = Namespace("api")

@member_ns.route("/member/register")
class MemberRegisterAPI(Resource):
    
    @member_ns.expect(member_input_model)
    def post(self):
        if Member.query.filter_by(username=member_ns.payload["username"]).first():
            response = {"message": "Username has been used"}
            return response, 401
        if Member.query.filter_by(username=member_ns.payload["email"]).first():
            response = {"message": "Email has been used"}
            return response, 401
        salt = generate_salt()
        password_hash = generate_password_hash(member_ns.payload["password"]+ salt)
        member = Member(username=member_ns.payload["username"], email=member_ns.payload["email"], password_hash=password_hash, salt=salt)
        db.session.add(member)
        db.session.commit()
        return 201

@member_ns.route("/member/login")
class MemberLoginAPI(Resource):
    
    @member_ns.expect(member_login_model)
    def post(self):
        member = Member.query.filter_by(username=member_ns.payload["username"]).first()
        if not member:
            return {"message": "User dose not exist"}, 401
        if not check_password_hash(member.password_hash, member_ns.payload["password"] + member.salt):
            return {"message": "Incorrect password"}, 401
        member_data = {"username": member.username, "id": member.id}
        access_token = create_access_token(identity=member, additional_claims=member_data)
        refresh_token = create_refresh_token(identity=member)
        response = jsonify({"message": "login successful", "id": member.id, "ok": True, "csrf_access_token":  get_csrf_token(access_token), "csrf_refresh_token": get_csrf_token(refresh_token)})
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)
        return response
    
@member_ns.route("/member/reset")
class MemberResetAPI(Resource):

    @member_ns.expect(reset_input_model)
    @member_ns.marshal_with(reset_output_model)
    def post(self):
        member = get_member_by_email(member_ns.payload["email"])
        if member:
            salt = generate_salt()
            password_hash = generate_password_hash(member_ns.payload["password"]+ salt)
            update_member_password_salt(member, password_hash, salt)
            return {"message": "ok"}, 200
        else: 
            return abort(400, "Email does not exist")

@member_ns.route("/members/<int:id>/tasks")
class Protected(Resource):

    @jwt_required()
    @member_ns.marshal_with(task_model)
    def get(self, id):
        member = get_member_by_id(id)
        if not member: abort(400, "Member not found")
        memberTasks = get_member_tasks(member)
        return memberTasks

