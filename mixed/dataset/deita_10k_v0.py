import nlp2
from datasets import load_dataset

dataset = load_dataset("hkust-nlp/deita-10k-v0", split='train')

chat_items = []
for i in dataset:
    chat_item = []
    for j in i['conversations']:
        if j['from'] == 'human':
            chat_item.append({"role": "user", "content": j['value']})
        else:
            chat_item.append({"role": "assistant", "content": j['value']})
    chat_items.append({"chat": chat_item})

nlp2.write_jsonl(chat_items, "./deita_10k_v0_chat.jsonl")
