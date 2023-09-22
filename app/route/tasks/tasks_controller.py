from flask_restx import Namespace ,Resource
from flask_jwt_extended import jwt_required
from ...extensions import db
from ...models import Task
from ...api_models import task_update_model, task_model
from .task_model import *
tasks_ns = Namespace("api/tasks")


@tasks_ns.route("/<int:id>")
class TaskAPI(Resource):

    @jwt_required()
    def delete(self, id):
        deleteTask(id)
        return {}, 204

    @jwt_required()
    @tasks_ns.expect(task_update_model)
    @tasks_ns.marshal_with(task_model)
    def put(self, id):
        task = Task.query.get(id)
        newTask = {
            "member_id": tasks_ns.payload.get("member_id"),
            "title": tasks_ns.payload.get("title"),
            "priority": tasks_ns.payload.get("priority"),
            "state": tasks_ns.payload.get("state"),
            "start": tasks_ns.payload.get("start"),
            "deadline": tasks_ns.payload.get("deadline"),
            "description": tasks_ns.payload.get("description")
        }
        for key, value in newTask.items():
            if value is not None:
                setattr(task, key, value)
        db.session.commit()
        return task, 200

@tasks_ns.route("")
class TaskListAPI(Resource):

    @jwt_required()
    @tasks_ns.expect(task_model)
    @tasks_ns.marshal_with(task_model)
    def post(self):
        newTask = getNewTask(tasks_ns)
        task = addTask(newTask)
        return task