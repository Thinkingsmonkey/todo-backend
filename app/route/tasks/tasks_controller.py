from flask_restx import Namespace ,Resource
from flask_jwt_extended import jwt_required
from ...api_models import task_update_model, task_model
from .tasks_model import *
tasks_ns = Namespace(name="Task", path="/api/tasks")


@tasks_ns.route("/<int:id>")
class TaskAPI(Resource):

    # @jwt_required()
    def delete(self, id):
        "Delete Task"
        task = get_task_by_id(id)
        if not task:
            return {"message": "Task does not exst"}, 404 
        delete_task(task)
        return {}, 204

    # @jwt_required()
    @tasks_ns.expect(task_update_model)
    @tasks_ns.marshal_with(task_model)
    def put(self, id):
        "Update Task"
        task = get_task_by_id(id)
        update_data = get_task_data(tasks_ns)
        task = update_task(task, update_data)
        return task, 200

@tasks_ns.route("") 
class TaskListAPI(Resource):

    # @jwt_required()
    @tasks_ns.expect(task_model)
    @tasks_ns.marshal_with(task_model)
    def post(self):
        "Create New Task"
        new_task = get_task_data(tasks_ns)
        task = add_task(new_task)
        return task