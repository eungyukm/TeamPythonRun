# Use a pipeline as a high-level helper
from transformers import pipeline

emotion_analyzer = pipeline("text-classification", model="nlp04/korean_sentiment_analysis_kcelectra")

# 테스트할 문장
texts = [
    "오늘 너무 행복해!",
    "기분이 우울하고 슬퍼.",
    "정말 화가 난다!",
    "놀라운 소식이야!",
    "무서워서 도망가고 싶어."
]

# 감정 분석 실행
results = emotion_analyzer(texts)

# 결과 출력
for text, result in zip(texts, results):
    print(f"문장: {text}")
    print(f"예측된 감정: {result['label']} (신뢰도: {result['score']:.4f})\n")