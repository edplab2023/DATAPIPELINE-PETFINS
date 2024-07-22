## 치료비 예측 모델 파이프라인
- 반려동물 건강정보를 기반으로 보험청구비를 예측하는 머신러닝 모델 파이프라인입니다.
- 

### Getting started
``` bash
run 
```

### 프로세스
- 재학습: (파라미터들)
- 배포: mlflow server에서 선택 -> 이미지 새로 태그바꿔서 빌드 -> 컨테이너 띄움 -> 로드 밸런싱 설정 -> Istio로 분배

- 결과를 바로 확인 가능한지?

### 시스템 구성도
- 사용자 요청 처리 백엔드 api
    - `/train`
    - `/inference`
    - `/statistics`


- 추론 api
- Experiment Tracking Server


### 평가지표(evaluation)
MSE: 이상치가 많다. (동물병원마다 같은 진료항목에 대해서도 치료비가 상이)



### 무중단 배포 전략


- 롤링 업데이트
- Blue/Green
- Canary
- 

### 부하테스트


### 기술스택
- Language: Python
- WebFramework: FastAPI
- ML Training: sklearn, LightGBM
- ML Serving: MLflow
- ML Experiment Tracking: MLflow
- Container: Docker
- CI/CD: Github Action, ArgoCD
- Container Orchestration: Kubernetes