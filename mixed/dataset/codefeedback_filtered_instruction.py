import nlp2
from datasets import load_dataset

dataset = load_dataset("m-a-p/CodeFeedback-Filtered-Instruction", split='train')

chat_items = []
for i in dataset:
    chat_item = []
    chat_item.append({"role": "user", "content": i['query']})
    chat_item.append({"role": "assistant", "content": i['answer']})
    chat_items.append({"chat": chat_item})

nlp2.write_jsonl(chat_items, "./codefeedback_filtered_instruction_chat.jsonl")