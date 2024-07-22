import requests
import json

# MLflow 서버의 URL
mlflow_tracking_uri = "http://localhost:5000"

# 검색할 모델 이름
model_name = "pet_insurance_claim_prediction"

# 검색 요청의 URL
search_url = f"{mlflow_tracking_uri}/api/2.0/mlflow/registered-models/search"

# 요청 파라미터 설정
params = {
    "filter": f"name = '{model_name}'",
    "max_results": 100
}

# GET 요청 보내기
response = requests.get(search_url, params=params)

# 응답 처리
if response.status_code == 200:
    model_info = response.json()
    print(json.dumps(model_info, indent=2))
else:
    print(f"Failed to search for models. Status code: {response.status_code}, Error: {response.text}")