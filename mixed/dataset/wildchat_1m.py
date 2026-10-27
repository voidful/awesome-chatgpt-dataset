import nlp2
from datasets import load_dataset

dataset = load_dataset("allenai/WildChat-1M", split='train')

chat_items = []
for i in dataset:
    chat_item = []
    for turn in i.get('conversation', []):
        role = turn.get('role', 'user')
        chat_item.append({"role": role, "content": turn.get('content', '')})
    chat_items.append({"chat": chat_item})

nlp2.write_jsonl(chat_items, "./wildchat_1m_chat.jsonl")
