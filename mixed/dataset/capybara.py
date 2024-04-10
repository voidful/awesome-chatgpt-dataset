import nlp2
from datasets import load_dataset

dataset = load_dataset("LDJnr/Capybara", split='train')

chat_items = []
for i in dataset:
    chat_item = []
    for j in i['conversation']:
        chat_item.append({"role": "user", "content": j['input']})
        chat_item.append({"role": "assistant", "content": j['output']})
    chat_items.append({"chat": chat_item})

nlp2.write_jsonl(chat_items, "./Capybara_chat.jsonl")
