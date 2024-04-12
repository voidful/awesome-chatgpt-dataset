import nlp2
from datasets import load_dataset

dataset = load_dataset("ssbuild/alpaca_auto_cot", split='train')

chat_items = []
for i in dataset:
    inst = i['instruction']
    input_text = i['input']
    chat = [
        {"role": "user", "content": f"""{inst}\n{input_text}""".strip()},
        {"role": "assistant", "content": i['output']}
    ]
    chat_items.append({"chat": chat})

nlp2.write_jsonl(chat_items, "./alpaca_auto_cot_chat.jsonl")
