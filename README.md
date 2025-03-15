# Portfolio_Data_analysis
데이터 분석 프로젝트 포트폴리오 정리

---
### 01. Project - 건강 데이터 분석을 통한 질병의 이해 및 건강 관리 적략 수립
- 프로젝트 소개
  - 비만 단계를 예측하는 모델을 생성하고, 비만에 큰 영향을 주는 변수를 파악함
  - 생활 습관 데이터를 클러스터링 하여, 생활 습관과 건강 상태간의 연관성을 파악함
  - t-검정을 수행하여, 생리학적 지표와 각 질병의 발병률 간에 통계적으로 유의미한 관련성이 있는지 분석함
  - statsmodel 패키지의 로지스틱 회귀를 이용하여 건강 지표가 질병의 발병률에 미치는 영향에 대해 분석함
  - scikit-learn 패키지의 로지스틱 회귀를 이용하여 질병 유병 여부를 예측하고, confusion matrix 와 ROC curve로 시각화함

---
### 02. Project - 학교 안전사고 분석 및 예방 전략 수립
- 프로젝트 소개
  - 각 요일·장소·학교급·계절·지역 등 다양한 요소에 따라 발생하는 학교 안전사고 패턴에 대해 분석함
  - 연관 분석을 활용하여 빈번히 나타나는 사고 패턴을 파악하고, 이를 방지하기 위한 전략 및 기대 효과를 제시함

- [project ppt](https://github.com/HongJunseong/Portfolio_data_analysis/blob/main/02-schoo_safe_analysis/%ED%95%99%EA%B5%90%20%EC%95%88%EC%A0%84%EC%82%AC%EA%B3%A0%20%EB%B6%84%EC%84%9D%20%EB%B0%8F%20%EC%98%88%EB%B0%A9%20%EC%A0%84%EB%9E%B5%20%EC%88%98%EB%A6%BD.pdf)

---
### 03. Project - 리스크 헷지 기반 ETF 추천 서비스
- 프로젝트 소개
  - 상관관계 분석을 통해 개인 투자자들이 시장 변동성에 대비해 안정적인 포트폴리오를 구성하도록 돕는 것을 목표로 함. 특히, 개별 주식보다 변동성이 낮고 다양한 섹터에 분산 투자된 ETF(Exchange-Traded Funds)를 분석 대상으로 삼아 보다 안정적인 헷징 효과를 제공하고자 함. 이를 통해 사용자는 특정 종목 선택 시 반대 경향성을 가진 ETF를 추천받아 리스크를 효과적으로 관리할 수 있을 것으로 기대됨
  - 리커드 척도을 활용한 설문조사를 생성하고, 이를 통해 사용자의 선택형 및 서술형 답변을 수집함
  - 서술형 응답 평가에 대한 한계점을 보완하기 위해 설문조사에 LLM을 결합하여 위험 점수를 계산하고, 이를 통해 사용자의 투자 성향을 도출함
  - 추천 기준을 정의하여 사용자의 투자 성향에 맞는 ETF를 추천할 수 있도록 구현함

- [vin github](https://github.com/HongJunseong/VIN)
- [vin notion](https://vigorous-helenium-94e.notion.site/00a485db6469497682d39715a07f7a19?v=ef02ec1ea67c43bdac9157c273b4203b)
- [서비스 시연 영상 유튜브](https://www.youtube.com/watch?v=FWQwvUAIn-Y)

---
### 04. Project - SNS 게시글 분석 기반 신뢰할 수 있는 식당 정보 도출
- 프로젝트 소개
  - sns의 무분별한 광고 속에서, 보다 신뢰성 있는 식당 정보를 제공함으로써 사용자의 만족도를 높이는 것을 목표로 함
  - 음식과 관련이 있는 키워드로 검색하여 나온 게시글들을 크롤링하고, LLM을 통해 게시글 본문 내용으로부터 식당명, 도로명 주소 등 주요 정보를 추출함
  - 데이터베이스로 MongoDB를 사용함
  - SMOTE로 광고·비광고 데이터의 불균형을 해소한 후, XGBoost, LIGHTGBM, TabNet을 이용하여 광고 판별 모델을 생성함
  - 광고로 판별된 게시글들을 추천 식당 목록에서 제외하여 사용자에게 더욱 신뢰할 수 있는 정보를 제공함
  - Kakaomap API를 활용하여, 추출된 데이터들을 지도상에 표기함
 
- [프로젝트 요약](https://github.com/HongJunseong/Portfolio_data_analysis/blob/main/04-foodfinder_by_sns/README.md)
