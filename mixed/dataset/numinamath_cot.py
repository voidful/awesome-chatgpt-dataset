import nlp2
from datasets import load_dataset

dataset = load_dataset("AI-MO/NuminaMath-CoT", split='train')

chat_items = []
for i in dataset:
    chat = [
        {"role": "user", "content": i['problem']},
        {"role": "assistant", "content": i['solution']}
    ]
    chat_items.append({"chat": chat})

nlp2.write_jsonl(chat_items, "./numinamath_cot_chat.jsonl")
