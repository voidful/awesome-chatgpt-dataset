import nlp2
from datasets import load_dataset
import json

alpaca_gpt4_dataset = load_dataset("vicgalle/alpaca-gpt4")

chat_items = []


def transform_to_chat_format(example):
    if len(example['input'].strip()) > 0:
        chat_items.append({"chat": [
            {"role": "user", "content": example['instruction'] + "\n" + example['input']},
            {"role": "assistant", "content": example['output']}
        ]})
    else:
        chat_items.append({"chat": [
            {"role": "user", "content": example['instruction']},
            {"role": "assistant", "content": example['output']}
        ]})


alpaca_gpt4_dataset = alpaca_gpt4_dataset.map(transform_to_chat_format)

nlp2.write_jsonl(chat_items, "./alpaca_gpt4_chat.jsonl")
