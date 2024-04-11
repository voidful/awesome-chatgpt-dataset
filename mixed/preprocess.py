from datasets import load_dataset, concatenate_datasets
import nlp2

data_list = []
for dataset_name in nlp2.get_files_from_dir('./dataset', match='jsonl'):
    print(dataset_name)
    data_list.append(load_dataset("json", data_files=dataset_name)['train'])

ds = concatenate_datasets(data_list)
ds.shuffle()
print(ds, ds[0])


def get_hash(example):
    return {"hash": hash(str(example["chat"]))}


def check_uniques(example, uniques):
    if example["hash"] in uniques:
        uniques.remove(example["hash"])
        return True
    else:
        return False


ds = ds.map(get_hash)
uniques = set(ds.unique("hash"))
ds_filter = ds.filter(check_uniques, fn_kwargs={"uniques": uniques})
print(ds_filter)

ds_filter.push_to_hub('voidful/mixed_chat')