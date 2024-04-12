import nlp2
from datasets import load_dataset

dataset = load_dataset("erfanzar/Xerxes-Instruct-700K", split='train')

chat_items = []
for i in dataset:
    chat_item = []
    for j in i['conversation']:
        chat_item.append({"role": j['role'], "content": j["content"]})
    chat_items.append({"chat": chat_item})

nlp2.write_jsonl(chat_items, "./xerxes_instruct.jsonl")
