import nlp2


nlp2.download_file("https://huggingface.co/datasets/MaggiePai/mental_health_counseling_conversations/raw/main/combined_dataset.jsonl",
                   "mental_health_counseling_conversations")

chat_items = []
for i in nlp2.read_jsonl("./mental_health_counseling_conversations/combined_dataset.jsonl"):
    chat = [
        {"role": "user", "content": i['Context']},
        {"role": "assistant", "content": i['Response']}
    ]
    chat_items.append({"chat": chat})

nlp2.write_jsonl(chat_items, "./mental_health_counseling_conversations_chat.jsonl")