import nlp2
from datasets import load_dataset

dataset = load_dataset("databricks/databricks-dolly-15k")

chat_items = []


def transform_to_chat_format(example):
    if len(example['context'].strip()) > 0:
        chat_items.append({"chat": [
            {"role": "user", "content": example['context'] + "\n" + example['instruction']},
            {"role": "assistant", "content": example['response']}
        ]})
    else:
        chat_items.append({"chat": [
            {"role": "user", "content": example['instruction']},
            {"role": "assistant", "content": example['response']}
        ]})


alpaca_gpt4_dataset = dataset.map(transform_to_chat_format)

nlp2.write_jsonl(chat_items, "./databricks_dolly_15k_chat.jsonl")