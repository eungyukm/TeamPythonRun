from transformers import pipeline
import torch

# CPU에서 실행되도록 설정
device = torch.device("cpu")

# 감정 분석 모델 명시적으로 지정
sentiment_analysis = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    device=device  # CPU에서 실행
)

result = sentiment_analysis("I love using Hugging Face!")
print(result)