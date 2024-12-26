from transformers import GPT2LMHeadModel, GPT2Tokenizer

model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

tokenizer.pad_token = tokenizer.eos_token

input_text = "I'm a little bit of a nerd."
inputs = tokenizer(input_text, return_tensors="pt", padding=True)

output = model.generate(
    **inputs,
    max_length=50,
    pad_token_id=tokenizer.eos_token_id,
    repetition_penalty=1.5,
    temperature=0.8,
    top_k=50,
    top_p=0.9,
    do_sample=True  # 샘플링 방식 사용
)

print(tokenizer.decode(output[0], skip_special_tokens=True))