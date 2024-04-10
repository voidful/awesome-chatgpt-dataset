import nlp2
from datasets import load_dataset

dataset = load_dataset("Open-Orca/SlimOrca",split='train')

chat_items = []
for i in dataset:
    chat_item = []
    for conv in i['conversations']:
        if conv['from'] == 'system':
            role = 'system'
        else:
            role = 'assistant' if conv['from'] == 'gpt' else 'user'
        chat_item.append({"role": role, "content": conv['value']})
    chat_items.append({"chat": chat_item})

nlp2.write_jsonl(chat_items, "./slim_orca_chat.jsonl")
