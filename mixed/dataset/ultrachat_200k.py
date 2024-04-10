import nlp2
from datasets import load_dataset

dataset = load_dataset("HuggingFaceH4/ultrachat_200k")

chat_items = []
for split in ['train_sft', 'test_sft']:
    for i in dataset[split]:
        chat_item = []
        for j in i['messages']:
            chat_item.append({"role": j['role'], "content": j['content']})
        chat_items.append({"chat": chat_item})

nlp2.write_jsonl(chat_items, "./ultrachat_200k_chat.jsonl")
