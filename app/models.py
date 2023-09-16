from .extensions import db 
import secrets
from sqlalchemy import func
from datetime import datetime, timedelta

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(500), nullable=False)
    salt = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    tasks = db.relationship("Task", back_populates="member", cascade="all, delete-orphan")

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey("member.id"), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    priority = db.Column(db.Enum('High', 'Medium', 'Low'), default="Medium")
    state = db.Column(db.Enum('Todo', 'Doing', 'Done'), default="Todo")
    start = db.Column(db.DateTime, server_default=func.current_timestamp())
    deadline = db.Column(db.DateTime, default=datetime.now() + timedelta(days=1))
    description = db.Column(db.Text, default="")
    member = db.relationship("Member", back_populates="tasks")


def generate_salt():
    return secrets.token_hex(16)
