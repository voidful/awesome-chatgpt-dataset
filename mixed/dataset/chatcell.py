import nlp2
from datasets import load_dataset

dataset = load_dataset("zjunlp/ChatCell-Instructions", split='train+test+validation')

chat_items = []
for i in dataset:
    chat = [
        {"role": "user", "content": i['source']},
        {"role": "assistant", "content": i['target']}
    ]
    chat_items.append({"chat": chat})

nlp2.write_jsonl(chat_items, "./chatcell.jsonl")
