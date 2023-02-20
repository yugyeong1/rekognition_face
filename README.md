# rekognition_face

https://docs.aws.amazon.com/ko_kr/rekognition/latest/dg/API_CompareFaces.html  
aws rekognition 의 얼굴 감지, 얼굴 인식 코드 구현 결과이다.  

postman 으로 사진 파일을 전달 받으면, 파일을 aws s3 에 저장하고,  
s3 에 저장한 img url 을 불러와 detect_faces, compare_faces 를 하여 결과값을 return 해준다.  



detect_faces  

![image](https://user-images.githubusercontent.com/104052659/219991172-6c8cef9e-c17b-4e34-8dc7-9a5ad5ea8c00.png)



compare_faces  

![image](https://user-images.githubusercontent.com/104052659/219991219-e84da424-6f64-43b6-83d0-78c96ab54af8.png)


