import nlp2
from datasets import load_dataset
import json

# If the dataset is gated/private, make sure you have run huggingface-cli login
dataset = load_dataset("voidful/wikihow_chat", split='train+test+validation')

chat_items = []
error_count = 0
for i in dataset['dialog']:
    try:
        chat_item = []
        data = json.loads(i)
        for d in data:
            chat_item.append({"role": d['role'], "content": d['content']})
        chat_items.append({'chat': chat_item})
    except:
        error_count += 1
        pass
print(f"error data: {error_count}")
nlp2.write_jsonl(chat_items, "./wikihow_chat.jsonl")
