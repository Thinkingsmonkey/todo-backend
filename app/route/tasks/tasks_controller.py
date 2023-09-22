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
        task = get_task_by_id(id)
        delete_task(task)
        return {}, 204

    @jwt_required()
    @tasks_ns.expect(task_update_model)
    @tasks_ns.marshal_with(task_model)
    def put(self, id):
        task = get_task_by_id(id)
        new_task = get_new_task(tasks_ns)
        task = update_task(task, new_task)
        return task, 200

@tasks_ns.route("")
class TaskListAPI(Resource):

    @jwt_required()
    @tasks_ns.expect(task_model)
    @tasks_ns.marshal_with(task_model)
    def post(self):
        new_task = get_new_task(tasks_ns)
        task = add_task(new_task)
        return task