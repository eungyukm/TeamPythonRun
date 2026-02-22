import numpy as np
import faiss
import time
from sentence_transformers import SentenceTransformer

# 사전 훈련된 SBERT 모델 로드
model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

# 문서 데이터셋
documents = [
    "안녕하세요! 무엇을 도와드릴까요?",
    "현재 날씨 정보를 확인해보세요!",
    "저는 AI 챗봇입니다.",
    "저는 한국어 문장을 이해하고 가장 적절한 응답을 제공합니다.",
    "안녕히 가세요! 또 만나요."
]

# 문서 임베딩 생성
document_embeddings = model.encode(documents)

# FAISS 인덱스 생성
index = faiss.IndexIDMap(faiss.IndexFlatIP(document_embeddings.shape[1]))
index.add_with_ids(np.array(document_embeddings, dtype=np.float32), np.array(range(len(documents))))

def search(query, k=5):
    t = time.time()
    query_vector = model.encode([query]).astype(np.float32)
    top_k = index.search(query_vector, k)
    print('검색 소요 시간: {:.4f}초'.format(time.time() - t))
    return [documents[_id] for _id in top_k[1].tolist()[0]]

# 검색 실행
while True:
    user_input = input("검색어를 입력하세요: ")
    if user_input.lower() in ["종료", "끝"]:
        print("검색을 종료합니다.")
        break
    results = search(user_input)
    print("검색 결과:")
    for result in results:
        print(f"\t{result}")