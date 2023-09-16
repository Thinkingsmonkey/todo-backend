from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_jwt_extended import JWTManager

api = Api() # 創建 restx 的 Api 實例，用以被調用
db = SQLAlchemy() # 創建 sqlalchem 實例，用以被調用
jwt = JWTManager() # 創建 jwt 實例，可被調用