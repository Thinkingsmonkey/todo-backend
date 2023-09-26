from ...extensions import db
from ...models import Task

def get_task_by_id(id):
  return Task.query.get(id)

def delete_task(task):
  db.session.delete(task)
  db.session.commit()

def add_task(newTask):
  task = Task(**newTask)
  db.session.add(task)    # 將物件加入到資料庫會話中
  db.session.commit()  
  return task

def update_task(task, new_task):
  for key, value in new_task.items():
    if value is not None:
      setattr(task, key, value)
  db.session.commit()
  return task

def get_task_data(tasks_ns):
  return {
      "member_id": tasks_ns.payload.get("member_id"),
      "title": tasks_ns.payload.get("title"),
      "priority": tasks_ns.payload.get("priority"),
      "state": tasks_ns.payload.get("state"),
      "start": tasks_ns.payload.get("start"),
      "deadline": tasks_ns.payload.get("deadline"), 
      "description": tasks_ns.payload.get("description") # 前端若傳送預設的空字串(text 無法設定預設值)
  }

