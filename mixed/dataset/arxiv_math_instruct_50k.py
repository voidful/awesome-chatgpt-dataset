import nlp2
from datasets import load_dataset

dataset = load_dataset("ArtifactAI/arxiv-math-instruct-50k", split='train')

chat_items = []
for i in dataset:
    chat_item = []
    chat_item.append({"role": "user", "content": i['question']})
    chat_item.append({"role": "assistant", "content": i['answer']})
    chat_items.append({"chat": chat_item})

nlp2.write_jsonl(chat_items, "./arxiv_math_instruct_50k_chat.jsonl")