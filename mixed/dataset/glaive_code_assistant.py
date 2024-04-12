import nlp2
from datasets import load_dataset

dataset = load_dataset("glaiveai/glaive-code-assistant",split='train')

chat_items = []
for i in dataset:
    chat = [
        {"role": "user", "content": i['question']},
        {"role": "assistant", "content": i['answer']}
    ]
    chat_items.append({"chat": chat})

nlp2.write_jsonl(chat_items, "./glaive_code_assistant.jsonl")
