import nlp2
from datasets import load_dataset

dataset = load_dataset("sujet-ai/Sujet-Finance-Instruct-177k", split='train')

chat_items = []
for i in dataset:
    chat = [
        {"role": "user", "content": i['inputs'] + "\n" + i['user_prompt']},
        {"role": "assistant", "content": i['answer']}
    ]
    chat_items.append({"chat": chat})

nlp2.write_jsonl(chat_items, "./sujet_finance_instruct.jsonl")
