# 바름 - 사용자 맞춤 건강기능 식품 관리 및 추천 서비스  

<div align="center">
  <img src="https://github.com/Now-Hyeok/Bareum/assets/84857521/51bcc669-f565-49d0-89ac-24aac876ac08" style="width:350px; height:350px">
</div>

## 개발환경
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white"> <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white"> <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=Bootstrap&logoColor=white"> <img src="https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=Vue.js&logoColor=white"> <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white"> <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white"> <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white"> <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white"> <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white"> <img src="https://img.shields.io/badge/Microsoft Azure-0078D4?style=for-the-badge&logo=Microsoft Azure&logoColor=white"> <img src="https://img.shields.io/badge/NGINX-009639?style=for-the-badge&logo=NGINX&logoColor=white"> <img src="https://img.shields.io/badge/Amazon EC2-FF9900?style=for-the-badge&logo=Amazon EC2&logoColor=white"> <img src="https://img.shields.io/badge/PWA-5A0FC8?style=for-the-badge&logo=PWA&logoColor=white">

## 프로젝트 개요

### 프로젝트 설명

KT Aivle School 빅프로젝트 프로젝트

### 프로젝트 기간 및 참여인원

- 2023.05.22 ~ 2023.07.03
- 7명

### 프로젝트 목표

인공지능 기반 사용자 맞춤 건강기능식품 관리 및 추천 서비스

## 화면 구성

| 로그인 | 제품 등록 | 영양소 및 제품 확인 | 제품 추천 | 정기배송&쇼핑 | 복용알림 | 커뮤니티 |
| --- | --- | --- | --- | --- | --- | --- |
| <img src="https://github.com/YEUNU/Bareum/assets/61678329/e3e36963-3651-4e25-a896-b31dd48ebcea" width="300px"> | <img src="https://github.com/YEUNU/Bareum/assets/61678329/99e1481b-b2db-498a-a17d-77d7d3c8232f" width="300px"> | <img src="https://github.com/YEUNU/Bareum/assets/61678329/c3095666-963e-4936-b91f-76bc05085af3" width="300px"> | <img src="https://github.com/YEUNU/Bareum/assets/61678329/7de67532-9b74-4ce6-b153-a581d0c22706" width="300px"> | <img src="https://github.com/YEUNU/Bareum/assets/61678329/e009ae9e-8f15-484f-b86f-127058dda06f" width="300px"> | <img src="https://github.com/YEUNU/Bareum/assets/61678329/4e638c86-62ec-4498-b0e2-547be2e8c6bd" width="300px"> | <img src="https://github.com/YEUNU/Bareum/assets/61678329/8b0cb7cb-7001-4c88-ba6f-62d8b2a2e4bc" width="300px"> |  

| 결과 영상 |
|:-:|
|![결과 영상](https://github.com/YEUNU/Bareum/assets/61678329/56acb0e1-a7c3-442b-b8de-8c6d73013606)|


## 주요 기능 및 기대효과
<img src="https://github.com/Now-Hyeok/Bareum/assets/84857521/33cbfba2-77eb-428c-ac1b-07f7576e5c7f">



## AI
### OCR
- Clova AI 팀의 CRAFT와 deep-text-recognition-benchmark 논문을 참조하여 OCR모델
- OCR 기능의 성능을 개선하기 위해 코사인 유사도 검증을 사용하여 데이터베이스와 직접적으로 유사도를 확인하여 정확도를 높임

#### 학습 데이터
- 한글 데이터 "AI Hub 다양한 형태의 한글 문자 OCR"
- 영문 데이터 "Text OCR"
  
| 한글 데이터 | 영문 데이터 |
|---| --- |
| https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=91 | https://www.kaggle.com/datasets/robikscube/textocr-text-extraction-from-images-dataset |

#### 학습 결과
| 학습 결과 |
| --- |
| <img src="https://github.com/AIVLE-School-Third-Big-Project/AI_07_28/assets/61678329/e9690067-7a3c-48e7-b757-6e64f545feeb" width="320px"> |

### 추천 
- Pycaret을 활용하여 데이터에 적합한 모델 XGBoost 사용
- Optuna를 활용하여 XGBoost Fine-Tuning
  
#### 학습 데이터
- 식품의약품안전처 기반으로 만들어진 랜덤 50만개 데이터

#### 학습 결과
| 학습 결과 |
| --- |
| <img src="https://github.com/AIVLE-School-Third-Big-Project/AI_07_28/assets/61678329/9dd4caa7-01fc-444e-bee9-90d16dcf5698" width="320px"> |

### 감정 분석
- KoBert 토크나이저 활용
- 2 Layers Bi-LSTM + Conv1D 구조
  
#### 학습 데이터
- 네이버 쇼핑 크롤링 리뷰 데이터 29,063

#### 학습 결과
| 학습 결과 |
| --- |
| <img src="https://github.com/AIVLE-School-Third-Big-Project/AI_07_28/assets/61678329/7ae5a899-76fa-441f-a326-c69c60e7ac1a" width="320px"> |

| 워드클라우드 결과 긍정  | 워드클라우드 결과 부정 | 
| --- | --- |
| <img src="https://github.com/AIVLE-School-Third-Big-Project/AI_07_28/assets/61678329/29570820-93b2-453f-8b5a-d5914e2940b6" width="320px"> | <img src="https://github.com/AIVLE-School-Third-Big-Project/AI_07_28/assets/61678329/5b6a359e-b1a0-4ec7-bb31-855d5c52d273" width="320px"> |


