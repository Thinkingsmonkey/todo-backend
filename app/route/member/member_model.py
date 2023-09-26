from ...models import Member
from ...extensions import db
import secrets

def generate_salt():
  return secrets.token_hex(16)

def get_member_by_id(id):
  return Member.query.filter_by(id=id).first()

def get_member_tasks(member):
  return member.tasks

def get_member_by_username(username):
  return Member.query.filter_by(username=username).first()

def get_member_by_email(email):
  return Member.query.filter_by(email=email).first()

def addMember(username, email, password_hash, salt):
  member = Member(username=username, email=email, password_hash=password_hash, salt=salt)
  db.session.add(member)
  db.session.commit()


def update_member_password_salt(member, password_hash, salt):
  member.password_hash = password_hash
  member.salt = salt
  db.session.commit()