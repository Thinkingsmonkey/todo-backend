from ...extensions import db
from ...models import Task

def deleteTask(id):
  task = Task.query.get(id)
  db.session.delete(task)
  db.session.commit()

def addTask(newTask):
  task = Task(**newTask)
  db.session.add(task)    # 將物件加入到資料庫會話中
  db.session.commit()  
  return task

def getNewTask(tasks_ns):
  return {
      "member_id": tasks_ns.payload.get("member_id"),
      "title": tasks_ns.payload.get("title"),
      "priority": tasks_ns.payload.get("priority"),
      "state": tasks_ns.payload.get("state"),
      "start": tasks_ns.payload.get("start"),
      "deadline": tasks_ns.payload.get("deadline"), 
      "description": tasks_ns.payload.get("description") # 前端若傳送預設的空字串(text 無法設定預設值)
  }

