import nlp2
from datasets import load_dataset
import json

alpaca_gpt4_dataset = load_dataset("Open-Orca/OpenOrca")

chat_items = []


def transform_to_chat_format(example):
    if len(example['system_prompt'].strip()) > 0:
        chat_items.append({"chat": [
            {"role": "user", "content": example['system_prompt'] + "\n" + example['question']},
            {"role": "assistant", "content": example['response']}
        ]})
    else:
        chat_items.append({"chat": [
            {"role": "user", "content": example['question']},
            {"role": "assistant", "content": example['response']}
        ]})


alpaca_gpt4_dataset = alpaca_gpt4_dataset.map(transform_to_chat_format)

nlp2.write_jsonl(chat_items, "./openorca_chat.jsonl")
