from ...models import Member


def get_member_by_id(id):
  return Member.query.filter_by(id=id).first()

def get_member_tasks(member):
  return member.tasks