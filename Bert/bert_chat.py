import numpy as np
from sentence_transformers import SentenceTransformer, util

# 사전 훈련된 한국어 지원 SBERT 모델 로드
model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

# 질문과 답변 데이터셋
qa_pairs = {
    "안녕하세요": "안녕하세요! 무엇을 도와드릴까요?",
    "오늘 날씨 어때?": "현재 날씨 정보를 확인해보세요!",
    "이름이 뭐야?": "저는 AI 챗봇입니다.",
    "무엇을 할 수 있어?": "저는 한국어 문장을 이해하고 가장 적절한 응답을 제공합니다.",
    "잘가": "안녕히 가세요! 또 만나요."
}

# 질문 벡터화
questions = list(qa_pairs.keys())
question_embeddings = model.encode(questions, convert_to_tensor=True)

# 코사인 유사도 계산 함수
def cos_sim(A, B):
    return np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))

# 가장 유사한 답변 찾기
def return_answer(question):
    embedding = model.encode(question)
    similarities = [cos_sim(embedding, q_emb) for q_emb in model.encode(questions)]
    best_match_idx = np.argmax(similarities)
    if similarities[best_match_idx] > 0.6:
        return qa_pairs[questions[best_match_idx]]
    else:
        return "죄송합니다. 이해하지 못했어요. 다시 말씀해 주세요."

# 테스트
while True:
    user_input = input("당신: ")
    if user_input.lower() in ["종료", "끝"]:
        print("챗봇: 대화를 종료합니다.")
        break
    response = return_answer(user_input)
    print(f"챗봇: {response}")
