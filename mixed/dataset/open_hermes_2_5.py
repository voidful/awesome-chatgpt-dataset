import nlp2
from datasets import load_dataset

dataset = load_dataset("teknium/OpenHermes-2.5", split='train')

chat_items = []
for i in dataset:
    chat_item = []
    if i.get('system_prompt'):
        chat_item.append({"role": "system", "content": i['system_prompt']})
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

nlp2.write_jsonl(chat_items, "./open_hermes_2_5_chat.jsonl")
