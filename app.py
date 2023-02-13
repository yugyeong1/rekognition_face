from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

from config import Config
from resources.aws import RekognitionTest
# from config import Config


app = Flask(__name__)
# 환경변수 셋팅
app.config.from_object(Config)

api = Api(app)

# 경로와 리소스(API코드)를 연결한다.
api.add_resource(RekognitionTest, '/aws')



if __name__ == '__main__' :
    app.run()