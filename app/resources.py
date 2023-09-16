from flask_restx import Resource, Namespace
from flask_jwt_extended import create_access_token, set_access_cookies
from flask_jwt_extended import create_refresh_token, set_refresh_cookies
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_csrf_token
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from .api_models import *
from .models import generate_salt, Member, Task
from flask import jsonify, abort

# 類似 blueprint 設一個 url_prefix = "/api" 的意思
nspace = Namespace("api")


@nspace.route("/member/register")
class MemberRegisterAPI(Resource):
    
    @nspace.expect(member_input_model)
    @nspace.marshal_with(member_output_model)
    def post(self):
        if Member.query.filter_by(username=nspace.payload["username"]).first():
            response = {"message": "username has been used"}
            return response, 401
        salt = generate_salt()
        password_hash = generate_password_hash(nspace.payload["password"]+ salt)
        member = Member(username=nspace.payload["username"], email=nspace.payload["email"], password_hash=password_hash, salt=salt)
        db.session.add(member)
        db.session.commit()
        return member, 201

@nspace.route("/member/login")
class MemberLoginAPI(Resource):
    
    @nspace.expect(member_login_model)
    def post(self):
        member = Member.query.filter_by(username=nspace.payload["username"]).first()
        if not member:
            return {"error": "User dose not exist"}, 401
        if not check_password_hash(member.password_hash, nspace.payload["password"] + member.salt):
            return {"error": "Incorrect password"}, 401
        member_data = {"username": member.username, "id": member.id}
        access_token = create_access_token(identity=member, additional_claims=member_data)
        refresh_token = create_refresh_token(identity=member)
        response = jsonify({"message": "login successful", "id": member.id, "ok": True, "csrf_access_token":  get_csrf_token(access_token), "csrf_refresh_token": get_csrf_token(refresh_token)})
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)
        return response
    
@nspace.route("/member/reset")
class MemberResetAPI(Resource):

    @nspace.expect(reset_input_model)
    @nspace.marshal_with(reset_output_model)
    def post(self):
        member = Member.query.filter_by(email=nspace.payload["email"]).first()
        if member:
            salt = generate_salt()
            password_hash = generate_password_hash(nspace.payload["password"]+ salt)
            member.password_hash = password_hash
            member.salt = salt
            db.session.commit()
            return {"message": "ok"}, 200
        else: 
            return {"message": "Email does not exist"}

@nspace.route("/members/<int:id>/tasks")
class Protected(Resource):

    @jwt_required()
    @nspace.marshal_with(task_model)
    def get(self, id):
        member = Member.query.filter_by(id=id).first()
        if not member: abort(400, "Member not found")
        memberTasksById = member.tasks
        return memberTasksById


@nspace.route("/tasks/<int:id>")
class TaskAPI(Resource):

    @jwt_required()
    def delete(self, id):
        #! 可增加 error handle
        task = Task.query.get(id)
        db.session.delete(task)
        db.session.commit()
        return {}, 204

    @jwt_required()
    @nspace.expect(task_update_model)
    @nspace.marshal_with(task_model)
    def put(self, id):
        #! 可增加 error handle
        task = Task.query.get(id)
        newTask = {
            "member_id": nspace.payload.get("member_id"),
            "title": nspace.payload.get("title"),
            "priority": nspace.payload.get("priority"),
            "state": nspace.payload.get("state"),
            "start": nspace.payload.get("start"),
            "deadline": nspace.payload.get("deadline"),
            "description": nspace.payload.get("description")
        }
        for key, value in newTask.items():
            if value is not None:
                setattr(task, key, value)
        db.session.commit()
        return task, 200

@nspace.route("/tasks")
class TaskListAPI(Resource):

    @jwt_required()
    @nspace.expect(task_model)
    @nspace.marshal_with(task_model)
    def post(self):
        newTask = {
            "member_id": nspace.payload.get("member_id"),
            "title": nspace.payload.get("title"),
            "priority": nspace.payload.get("priority"),
            "state": nspace.payload.get("state"),
            "start": nspace.payload.get("start"),
            "deadline": nspace.payload.get("deadline"), 
            "description": nspace.payload.get("description") # 前端若傳送預設的空字串(text 無法設定預設值)
        }
        task = Task(**newTask)
        db.session.add(task)    # 將物件加入到資料庫會話中
        db.session.commit()  
        return task
