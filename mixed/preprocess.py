from datasets import load_dataset, concatenate_datasets
import argparse

def load_and_concatenate_data():
    data_list = []
    for dataset_name in nlp2.get_files_from_dir('./dataset', match='jsonl'):
        print(dataset_name)
        data_list.append(load_dataset("json", data_files=dataset_name)['train'])
    ds = concatenate_datasets(data_list)
    ds = ds.shuffle()
    print(ds, ds[0])
    return ds

def add_hash(ds):
    return ds.map(lambda example: {"hash": hash(str(example["chat"]))})

def filter_unique(ds):
    uniques = set(ds.unique("hash"))
    return ds.filter(lambda example, uniques=uniques: check_uniques(example, uniques), batched=True)

def check_uniques(example, uniques):
    if example["hash"] in uniques:
        uniques.remove(example["hash"])
        return True
    else:
        return False

def main(dataset_name):
    ds = load_and_concatenate_data()
    ds = add_hash(ds)
    ds = filter_unique(ds)
    ds.push_to_hub(dataset_name, private=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process and push dataset to Hugging Face's Dataset Hub.")
    parser.add_argument('dataset_name', type=str, help='The name of the dataset repository on Hugging Face Hub')
    args = parser.parse_args()
    main(args.dataset_name)
