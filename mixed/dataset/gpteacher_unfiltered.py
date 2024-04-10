import nlp2
from datasets import load_dataset

dataset = load_dataset("ewof/gpteacher-unfiltered")

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


alpaca_gpt4_dataset = dataset.map(transform_to_chat_format)

nlp2.write_jsonl(chat_items, "./gpteacher_chat.jsonl")