import json

import nlp2

chat_items = []

nlp2.download_file("https://huggingface.co/datasets/RUCKBReasoning/TableLLM-SFT/resolve/main/fetaqa.jsonl",
                   "TableLLM")
for i in nlp2.read_jsonl("./TableLLM/fetaqa.jsonl"):
    chat = [
        {"role": "user", "content": i['prompt']},
        {"role": "assistant", "content": i['response']}
    ]
    chat_items.append({"chat": chat})

nlp2.download_file("https://huggingface.co/datasets/RUCKBReasoning/TableLLM-SFT/raw/main/spider.jsonl",
                   "TableLLM")
for i in nlp2.read_jsonl("./TableLLM/spider.jsonl"):
    chat = [
        {"role": "user", "content": i['prompt']},
        {"role": "assistant", "content": i['response']}
    ]
    chat_items.append({"chat": chat})

nlp2.download_file("https://huggingface.co/datasets/RUCKBReasoning/TableLLM-SFT/resolve/main/table-op.jsonl",
                   "TableLLM")
for i in nlp2.read_jsonl("./TableLLM/table-op.jsonl"):
    chat = [
        {"role": "user", "content": i['prompt']},
        {"role": "assistant", "content": i['response']}
    ]
    chat_items.append({"chat": chat})

nlp2.download_file("https://huggingface.co/datasets/RUCKBReasoning/TableLLM-SFT/resolve/main/tatqa.jsonl",
                   "TableLLM")
for i in nlp2.read_jsonl("./TableLLM/tatqa.jsonl"):
    chat = [
        {"role": "user", "content": i['prompt']},
        {"role": "assistant", "content": i['response']}
    ]
    chat_items.append({"chat": chat})

nlp2.download_file("https://huggingface.co/datasets/RUCKBReasoning/TableLLM-SFT/resolve/main/wikisql.jsonl",
                   "TableLLM")
for i in nlp2.read_jsonl("./TableLLM/wikisql.jsonl"):
    chat = [
        {"role": "user", "content": i['prompt']},
        {"role": "assistant", "content": i['response']}
    ]
    chat_items.append({"chat": chat})

nlp2.download_file("https://huggingface.co/datasets/RUCKBReasoning/TableLLM-SFT/resolve/main/wtq.jsonl",
                   "TableLLM")
for i in nlp2.read_jsonl("./TableLLM/wtq.jsonl"):
    chat = [
        {"role": "user", "content": i['prompt']},
        {"role": "assistant", "content": i['response']}
    ]
    chat_items.append({"chat": chat})

nlp2.write_jsonl(chat_items, "./tableLLM_SFT_chat.jsonl")
