import nlp2
from datasets import load_dataset

dataset = load_dataset("allenai/tulu-v2-sft-mixture", split='train')

chat_items = []
for i in dataset:
    chat_item = []
    for j in i['messages']:
        if j['role'] == 'user':
            chat_item.append({"role": "user", "content": j['content']})
        else:
            chat_item.append({"role": "assistant", "content": j['content']})
    chat_items.append({"chat": chat_item})

nlp2.write_jsonl(chat_items, "./tulu_v2_sft_mixture_chat.jsonl")
