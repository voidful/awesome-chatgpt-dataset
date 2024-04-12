import nlp2
from datasets import load_dataset

dataset = load_dataset("MBZUAI/LaMini-instruction", split='train')

chat_items = []
for i in dataset:
    chat = [
        {"role": "user", "content": i['instruction']},
        {"role": "assistant", "content": i['response']}
    ]
    chat_items.append({"chat": chat})

nlp2.write_jsonl(chat_items, "./laMini_instruction_chat.jsonl")
