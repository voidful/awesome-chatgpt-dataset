import nlp2
from datasets import load_dataset

dataset = load_dataset("erfanzar/Flan-GPT4", split='train')

chat_items = []
for i in dataset:
    chat = [
        {"role": "system", "content": i['system']},
        {"role": "user", "content": i['instruction']},
        {"role": "assistant", "content": i['response']}
    ]
    chat_items.append({"chat": chat})

nlp2.write_jsonl(chat_items, "./flan_gpt4_chat.jsonl")
