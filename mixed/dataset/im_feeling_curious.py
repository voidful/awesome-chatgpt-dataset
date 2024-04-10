import nlp2
from datasets import load_dataset

dataset = load_dataset("xiyuez/im-feeling-curious", split='train')

chat_items = []
for i in dataset:
    chat_item = []
    chat_item.append({"role": "user", "content": i['question']})
    chat_item.append({"role": "assistant", "content": i['answer']})
    chat_items.append({"chat": chat_item})

nlp2.write_jsonl(chat_items, "./im_feeling_curious_chat.jsonl")
