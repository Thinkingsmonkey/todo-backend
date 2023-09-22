from ...extensions import db
from ...models import Task

def deleteTask(id):
  task = Task.query.get(id)
  db.session.delete(task)
  db.session.commit()