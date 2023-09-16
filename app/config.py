import os
import datetime

class Config():
  TEMPLATES_AUTO_RELOAD = True
  ERROR_404_HELP = False

  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')  # 部署環境使用
  # SQLALCHEMY_DATABASE_URI = "mysql://root:12345678@localhost/todo"  # 開發環境使用
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  JWT_SECRET_KEY = os.environ.get('JWT_SECRET') # 部署環境使用
  # JWT_SECRET_KEY = "this secret key" # 開發環境使用
  JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=60)
  JWT_TOKEN_LOCATION = ["headers", "cookies"]  
  JWT_CSRF_IN_COOKIES = False


  JWT_COOKIE_SECURE = True  # Secure 屬性
  JWT_COOKIE_SAMESITE = 'None'  # SameSite 屬性