import nlp2
from datasets import load_dataset

dataset = load_dataset("robinsmits/ChatAlpaca-20K", split='original')

chat_items = []
for i in dataset:
    chat_item = []
    for j in i['messages']:
        chat_item.append({"role": j['role'], "content": j['content']})
    chat_items.append({"chat": chat_item})

nlp2.write_jsonl(chat_items, "./chatAlpaca_chat.jsonl")
