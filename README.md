# 김영민 — AI 모델을 현장이 믿고 쓰는 서비스로 완성하는 엔지니어

LLM 문서 추출, 24시간 운영 인식 시스템의 검증 체계, 해석 가능한 기계학습 연구. 세 프로젝트의 공통점은 결과마다 근거를 남겨 사람이 검증할 수 있게 만든 것입니다.

## 프로젝트

| | 문제 | 내가 한 것 | 결과 | 역할·기간 |
|---|---|---|---|---|
| [1. LLM 문서 추출 파이프라인](projects/01-kisti-dart-extractor.md) | 사업보고서 수백 건에서 연구개발 기술과 투자 계획을 수작업으로 옮기던 연구팀 | 페이지 단위 파싱과 JSON 스키마 강제로 항목마다 근거 인용문과 쪽 번호가 붙는 추출기 설계 | 340여 건 처리, 통합 항목 183,398건 적재, 인수인계 후 이관 | 단독 개발, 한국과학기술정보연구원, 2025.08~11 |
| [2. LiDAR 인식 시스템 검증 체계](projects/02-gsi-lidar-validation.md) | 오탐을 고치면 다른 장면이 깨지는지 알 수 없던 항만 크레인용 인식 시스템 | 현장 데이터 리플레이 회귀 테스트 20건과 지연 p95/p99 CI 게이트, AI 코딩 에이전트에도 같은 게이트 적용 | 6개월간 PR 95건 통과, 원인·개선을 결정 기록으로 문서화 | 검증·CI 주도, 지에스아이 연구소, 2026.03~ |
| [3. 양극재 성능 예측과 원인 해석](projects/03-battery-ml.md) | 조성과 공정이 얽혀 실험만으로 최적 조건을 찾기 어려운 배터리 소재 | 약 500건 데이터로 XGBoost 예측, SHAP 해석, 합성 데이터 10만 건으로 후보 탐색 | R² 0.82, 유효 구간 규명, 학회 발표 2회, SCIE 저널 투고 | 석사 연구, 2024.01~2026.02 |

## 그 외

2023 전력사용량 예측 AI 경진대회(DACON, 한국에너지공단) 1,233팀 중 10위(2인 팀, 피처 설계·모델) · 나인와트 SW개발팀 인턴 10개월(ResNet 분류, XGBoost 예측 모델을 웹앱에 통합) · 데이터분석준전문가(ADsP) · OPIc IM1

## 발표·논문

- StatPhys29 국제 통계물리학회 포스터 발표 (이탈리아 피렌체, 2025.07)
- 한국물리학회 포스터 발표
- "Reliability-aware machine learning for optimizing Ni-rich cathode synthesis", Surfaces and Interfaces(SCIE) 공동 제1저자 투고, 심사 중

## 기술

Python, PyTorch, scikit-learn, XGBoost, SHAP, OpenAI API, Ollama, PostgreSQL, Docker, GitHub Actions, pytest, FastAPI, React
