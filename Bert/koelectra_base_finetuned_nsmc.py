from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline

MODEL_NAME = "monologg/koelectra-base-finetuned-nsmc"

# 토크나이저와 모델 로드
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

# 분류 파이프라인 생성
pipe = TextClassificationPipeline(
    model=model,
    tokenizer=tokenizer,
    framework='pt',         # PyTorch
    return_all_scores=True  # 모든 라벨의 점수를 반환
)


def sentiment_predict(sentence: str, pipeline=pipe):
    """
    입력 문장을 받아서 pipeline을 통해 긍정/부정 스코어를 계산하고,
    최종 라벨(positive/negative)을 반환하는 함수
    """
    # 결과 형태 예: [{'label': 'LABEL_0', 'score': 0.1234}, {'label': 'LABEL_1', 'score': 0.8766}]
    result = pipeline(sentence)[0]

    # label별 점수를 딕셔너리 형태로 변환
    scores = {res['label']: res['score'] for res in result}

    # 이 모델의 경우 LABEL_0=부정(negative), LABEL_1=긍정(positive)으로 알려져 있습니다.
    label_0_score = scores.get('LABEL_0', 0.0)
    label_1_score = scores.get('LABEL_1', 0.0)

    # 더 높은 쪽을 최종 라벨로 결정
    predicted_label = 'positive' if label_1_score >= label_0_score else 'negative'

    return predicted_label, scores


if __name__ == "__main__":
    test_sentences = [
        "이 영화 정말 재미있게 봤어요!",
        "내용이 지루하고 별로였어요.",
        "배우 연기는 좋았지만 스토리가 아쉬웠어요.",
        "최고의 영화 중 하나입니다.",
        "생각보다 나쁘진 않았어요."
    ]

    for sentence in test_sentences:
        label, score_dict = sentiment_predict(sentence)
        print(f"문장: {sentence}")
        print(f"예측 라벨: {label} | 세부 스코어: {score_dict}\n")
