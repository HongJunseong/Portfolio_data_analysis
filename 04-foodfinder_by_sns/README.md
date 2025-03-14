![image](https://github.com/user-attachments/assets/1351bef9-d347-4607-9ffb-57dc75f5ecef)contents_DB -> MongoDB 관리 코드

crawling_instagram -> selenium을 통한 sns 게시글 크롤링 코드

map_api -> 추출된 데이터와 kakaomap api를 통해 지도 생성 및 마크 표시

전처리 과정을 통해 얻은 3 개의 변수를 기반으로 광고 분류 모델을 구축하기 위해 머신러닝과 딥러닝을 활용하였다.
XGBoost(Ver. 2.1.3), LightGBM(Ver. 4.5.0), TabNet(Ver. 4.1.0)의 총 3가지 Classifier을 사용하였다.
<br/>
XGBoost와 LightGBM은 scikit-learn에서 제공하는 GridSearchCV를 사용하여 최적 파라미터를 구했고,
TabNet은 optuna 라이브러리를 활용하여 최적 파라미터를 구하였다.
각 예측 모델의 최적 하이퍼 파라미터 탐색 및 교차 검증을 수행한 결과는 아래의 표과 같다.
<br/>

![image](https://github.com/user-attachments/assets/615ef315-3f30-4ff7-8e9e-150c9b6a1c5d)

