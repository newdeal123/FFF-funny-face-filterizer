import cv2

# 얼굴 감지기 초기화
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 이미지 불러오기
image = cv2.imread('img/elon_musk.jpg')

# 이미지를 흑백으로 변환
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 얼굴 감지
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# 얼굴 영역에 블러 필터 적용
for (x, y, w, h) in faces:
    face_roi = image[y:y+h, x:x+w]
    blurred_face = cv2.GaussianBlur(face_roi, (99, 99), 30)
    image[y:y+h, x:x+w] = blurred_face


# 결과 이미지 출력
cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
