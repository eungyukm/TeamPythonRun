import torch
from transformers import BertTokenizer, BertForMaskedLM, pipeline
from transformers import AutoModelForMaskedLM

# 1) 토크나이저와 모델 로드
tokenizer = BertTokenizer.from_pretrained('bert-large-uncased')
model = AutoModelForMaskedLM.from_pretrained('bert-large-uncased')

# 2) 모델을 평가(evaluation) 모드로 전환
model.eval()

# 예시 문장
text = "Soccer is a really fun [MASK]."

# 토크나이즈 및 텐서 변환
inputs = tokenizer(text, return_tensors='pt')  # 'pt'는 PyTorch 텐서로 반환

print("Input IDs:", inputs['input_ids'])
print("Token Type IDs:", inputs['token_type_ids'])
print("Attention Mask:", inputs['attention_mask'])

# Fill-Mask 파이프라인 생성
fill_mask = pipeline("fill-mask", model=model, tokenizer=tokenizer)

# 예시 1
result1 = fill_mask("Soccer is a really fun [MASK].")
print(result1)

# 예시 2
result2 = fill_mask("The Avengers is a really fun [MASK].")
print(result2)

# 예시 3
result3 = fill_mask("I went to [MASK] this morning.")
print(result3)
