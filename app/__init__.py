from flask import Flask
from .extensions import api, db, jwt
from .resources import nspace
from .models import Member
from flask_cors import CORS
from .config import Config

def create_app():
    application = Flask(__name__)
    app = application
    app.config.from_object(Config)
    api.init_app(app)
    db.init_app(app)
    jwt.init_app(app)
    CORS(app, supports_credentials=True)

    
    # 在創建 JWT 時將傳入的使用者物件( SQLAlchemy 的物件)，轉化為 JSON
    # 回傳將成為 indentity 身分訊息放進 JSON 中一起被轉化
    @jwt.user_identity_loader
    def user_identity_lookup(member):
        return member.id

    # 在驗證 JWT 的路由中，檢驗 Member.query.filter_by(id=identity).first() 是否存在
    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_payload):
        print()
        identity = jwt_payload["sub"]
        return Member.query.filter_by(id=identity).first()

    api.add_namespace(nspace)
    return app