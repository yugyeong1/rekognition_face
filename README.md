## Amazon Rekognition 의 얼굴 감지, 얼굴 인식 코드 구현 결과  


노출이 되면 안되는 정보는 Config 파일에 저장하였고, 깃에는 config 파일을 제외하고 업로드 하였다.  
  


### detect_faces  
Rekognition을 사용하면 이미지에서 얼굴을 감지한 위치에 대한 정보뿐 아니라 눈의 위치와 같은 얼굴 표식과, 행복해 보이거나 슬퍼 보이는 등의 감지된 감정에 대한 정보를 가져올 수 있다.  
https://docs.aws.amazon.com/ko_kr/rekognition/latest/dg/faces-detect-images.html  
  
### compare_faces  
원본 이미지의 한 얼굴과 다른 이미지에서 감지된 얼굴도 비교할 수 있다.  
https://docs.aws.amazon.com/ko_kr/rekognition/latest/dg/API_CompareFaces.html  
  
##    
  

postman 으로 사진 파일을 전달 받으면, 파일을 aws s3 에 저장하고,  
s3 에 저장한 img url 을 불러와 detect_faces, compare_faces 를 하여 결과값을 return 해준다.  



### ✔ detect_faces  

![image](https://user-images.githubusercontent.com/104052659/219991172-6c8cef9e-c17b-4e34-8dc7-9a5ad5ea8c00.png)



### ✔ compare_faces  

![image](https://user-images.githubusercontent.com/104052659/219991219-e84da424-6f64-43b6-83d0-78c96ab54af8.png)


