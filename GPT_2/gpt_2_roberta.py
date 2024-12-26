from transformers import pipeline

# RoBERTa 기반 감정 분석 파이프라인 로드
classifier = pipeline("sentiment-analysis", model="roberta-base")

# 감정 분석 실행
result = classifier("This product is amazing!")
print(result)  # [{'label': 'POSITIVE', 'score': 0.9998}]