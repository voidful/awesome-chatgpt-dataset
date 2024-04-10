import nlp2
from datasets import load_dataset

dataset = load_dataset("HuggingFaceH4/CodeAlpaca_20K",split='train+test')

chat_items = []
for i in dataset:
    chat_item = [
        {"role": "user", "content": i['prompt']},
        {"role": "assistant", "content": i['completion']}
    ]
    chat_items.append({"chat": chat_item})

nlp2.write_jsonl(chat_items, "./codeAlpaca_chat.jsonl")
