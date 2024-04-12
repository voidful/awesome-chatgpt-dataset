import nlp2
from datasets import load_dataset

dataset = load_dataset("xzuyn/chatdoctor-200k-stripped",split='train')

chat_items = []
for i in dataset:
    chat = [
        {"role": "user", "content": i['instruction']+i['input']},
        {"role": "assistant", "content": i['output']}
    ]
    chat_items.append({"chat": chat})

nlp2.write_jsonl(chat_items, "./chatdoctor_200k_stripped_chat.jsonl")