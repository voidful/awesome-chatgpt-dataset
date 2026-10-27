import nlp2
from datasets import load_dataset

dataset = load_dataset("mlabonne/FineTome-100k", split='train')

chat_items = []
for i in dataset:
    chat_item = []
    for conv in i.get('conversations', []):
        sender = conv.get('from', '')
        if sender in ['human', 'user']:
            role = 'user'
        elif sender in ['gpt', 'assistant']:
            role = 'assistant'
        elif sender == 'system':
            role = 'system'
        else:
            role = 'user'
        chat_item.append({"role": role, "content": conv.get('value', '')})
    chat_items.append({"chat": chat_item})

nlp2.write_jsonl(chat_items, "./finetome_100k_chat.jsonl")
