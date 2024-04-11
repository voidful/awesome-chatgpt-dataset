import nlp2
import json

nlp2.download_file("https://raw.githubusercontent.com/wenhuchen/TheoremQA/main/theoremqa_test.json",
                   "theoremqa")
chat_items = []
with open("./theoremqa/theoremqa_test.json") as f:
    for i in json.load(f):
        chat = [
            {"role": "user", "content": i['Question']},
            {"role": "assistant", "content": str(i['Answer'])}
        ]
        chat_items.append({"chat": chat})
nlp2.write_jsonl(chat_items, "./theoremqa_chat.jsonl")