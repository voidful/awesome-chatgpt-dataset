import nlp2
from datasets import load_dataset

dataset = load_dataset("voidful/ruozhiba_s2t",split='train')

chat_items = []
for i in dataset:
    chat = [
        {"role": "user", "content": i['instruction']},
        {"role": "assistant", "content": i['output']}
    ]
    chat_items.append({"chat": chat})

nlp2.write_jsonl(chat_items, "./ruozhiba_chat.jsonl")