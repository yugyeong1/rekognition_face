import json
from flask import request
from flask_restful import Resource

from config import Config

from datetime import datetime

import boto3


class RekognitionTest(Resource) :
    def post(self) :

    # 1. 클라이언트가 보낸 데이터를 받는다.fl
        if 'photo' not in request.files :
            return {'error' : '파일을 업로드 하세요'}, 400

        file = request.files['photo']

    # 2. 사진을 먼저 S3에 저장
        ### 2-1. aws 콘솔로 가서 IAM 유저 만든다.(없으면 만든다)
        ### 2-2. s3 로 가서 이 프로젝트의 버킷을 만든다.
        ### 2-3. config.py 에 적어준다.

        ### 2-4. 파일명을 유니크하게 만든다.
        current_time = datetime.now()
        new_file_name = current_time.isoformat().replace(':','_')+'.jpg'

        file.filename = new_file_name
        
        ### 2-5. S3에 파일 업로드 한다.
        ###      파일 업로드하는 코드는! boto3라이브러리를
        ###      이용해서 업로드한다.
        ###      라이브러리가 설치안되어있으면, pip install boto3 로 설치한다.
        client = boto3.client('s3', 
                    aws_access_key_id = Config.ACCESS_KEY,
                    aws_secret_access_key = Config.SECRET_ACCESS)
        try :
            client.upload_fileobj(file,
                                    Config.S3_BUCKET,
                                    new_file_name,
                                    ExtraArgs = {'ACL':'public-read', 'ContentType' : file.content_type } )
        
        except Exception as e:
            return {'error' : str(e)}, 500


        # 3. S3에 저장된 사진을 detect_faces 한다
        #    (AWS Rekognition 이용)

        client = boto3.client('rekognition',
                    'ap-northeast-2',
                    aws_access_key_id=Config.ACCESS_KEY,
                    aws_secret_access_key = Config.SECRET_ACCESS)

        response = client.detect_faces(Image={'S3Object':{'Bucket':Config.S3_BUCKET, 'Name':new_file_name}}, Attributes=['ALL'])

        print(response)

        # 결과값 저장할 result_list 생성
        result_list = []
        for faceDetail in response['FaceDetails']:

            result_list.append("AgeRange" + str(faceDetail['AgeRange']))
            result_list.append("Gender: " + str(faceDetail['Gender']))
            result_list.append("Smile: " + str(faceDetail['Smile']))
            result_list.append("EyesOpen: " + str(faceDetail['EyesOpen']))
            result_list.append("Eyeglasses: " + str(faceDetail['Eyeglasses']))
            result_list.append("Emotions: " + str(faceDetail['Emotions'][0]))
            
            print(result_list)

            return { "result" : result_list }

        
        # 5. 결과를 클라이언트에 보내준다
        return {'result' : 'success'}            
