import nlp2
from datasets import load_dataset

dataset = load_dataset("m-a-p/COIG-CQIA", split='train')

chat_items = []
for i in dataset:
    user_content = i['instruction']
    if i.get('input') and len(i['input'].strip()) > 0:
        user_content = f"{user_content}\n{i['input']}".strip()
    chat = [
        {"role": "user", "content": user_content},
        {"role": "assistant", "content": i['output']}
    ]
    chat_items.append({"chat": chat})

nlp2.write_jsonl(chat_items, "./coig_cqia_chat.jsonl")
