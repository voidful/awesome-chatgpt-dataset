import nlp2
from datasets import load_dataset

dataset = load_dataset("meta-math/MetaMathQA", split='train')

chat_items = []
for i in dataset:
    chat_item = []
    chat_item.append({"role": "assistant", "content": i['query']})
    chat_item.append({"role": "user", "content": i['response']})
    chat_items.append({"chat": chat_item})

nlp2.write_jsonl(chat_items, "./meta_math_qa_chat.jsonl")
