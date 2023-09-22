from ...models import Member
from ...extensions import db

def get_member_by_id(id):
  return Member.query.filter_by(id=id).first()

def get_member_tasks(member):
  return member.tasks

def get_member_by_email(email):
  return Member.query.filter_by(email=email).first()

def update_member_password_salt(member, password_hash, salt):
  member.password_hash = password_hash
  member.salt = salt
  db.session.commit()