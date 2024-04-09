import json

import nlp2

nlp2.download_file("https://huggingface.co/datasets/jondurbin/airoboros-gpt4-m2.0/resolve/main/instructions.jsonl",
                   "airoboros_gpt4")

chat_items = []
for i in nlp2.read_jsonl("./airoboros_gpt4/instructions.jsonl"):
    chat = [
        {"role": "user", "content": i['instruction']},
        {"role": "assistant", "content": i['response']}
    ]
    chat_items.append({"chat": chat})

nlp2.write_jsonl(chat_items, "./airoboros_gpt4_chat.jsonl")
