# 노출이 되면 안되는 정보들은 config 파일에 변수로 저장을 한다.
class Config :
    # AWS RDS 주소를 넣어준다
    HOST = 'yh-db.chchigeg703r.ap-northeast-2.rds.amazonaws.com'
    # database 이름을 넣어준다
    DATABASE = 'photo_post'
    # 설정한 user 이름을 넣어준다
    DB_USER = 'photo_post_user'
    # 설정한 패스워드를 넣어준다.
    DB_PASSWORD = 'yh1234db'

    SALT = 'dskj29jkdsld'

    # JWT 관련 변수 셋팅
    JWT_SECRET_KEY = 'cocopig20230105##hello'
    JWT_ACCESS_TOKEN_EXPIRES = False
    PROPAGATE_EXCEPTIONS = True

    # AWS 관련 키
    ACCESS_KEY = 'AKIA57KIVK6XJZWKBFSB'
    SECRET_ACCESS = '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'
    
    # S3 버킷
    S3_BUCKET = 'rekognition123test'
    # S3 Location
    S3_LOCATION = 'https://rekognition123test.s3.ap-northeast-2.amazonaws.com/'
