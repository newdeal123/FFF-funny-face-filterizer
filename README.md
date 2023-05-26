# FFF (Funny Face Filterizer 🤗)

Face Filterizer는 OpenCV를 사용하여 얼굴 영역에 필터를 적용하는 간단한 프로젝트입니다. 이 프로젝트를 통해 이미지에서 얼굴을 감지하고 선택한 필터를 얼굴 영역에 적용하는 기능을 제공합니다.

<img src="./img/elon_musk.jpg" alt="원본 이미지" width="400" height="300">
<img src="./result/ret_elon_musk.png" alt="예시 이미지" width="500" height="400">

## 실행 방법

1. 프로젝트를 클론합니다.
```
git clone https://github.com/newdeal123/FFF-funny-face-filterizer
```
2. 필요한 라이브러리를 설치합니다.
```
pip install opencv-python
```
3.  이미지 파일을 준비합니다. `/img` 디렉토리에 필터를 적용할 이미지 파일을 넣어주세요. 확장자는 jpg를 지원합니다.

4. `face_filterizer.py` 스크립트를 실행합니다.

```
python face_filterizer.py
```

## 라이선스
이 프로젝트는 MIT 라이선스에 따라 배포됩니다. 자세한 내용은 LICENSE 파일을 참조하세요.