from importlib import import_module


def get_dataset(name: str):
    """load data from sklearn.datasets"""
    datasets = import_module('sklearn.datasets')
    load_dataset = getattr(datasets, 'load_' + name)
    dataset = load_dataset()
    return dataset


class DatasetInventory:
    """A class to encapsulate scikit-learn datasets"""
    names = set()

    def __init__(self, name: str):
        self.name = name
        ds = get_dataset(name)
        self.data, self.targ, self.cols, self.desc = (ds.get(x) for x in (
            'data', 'target', 'feature_names', 'DESCR'))
        if self.name not in DatasetInventory.names:
            DatasetInventory.names.add(self.name)

ds_names = 'boston', 'diabetes', 'digits', 'iris', 'wine'

ds_objects = (DatasetInventory(name=x) for x in ds_names)

_, diabetes = next(ds_objects), next(ds_objects)
_, diabetes, *_ = ds_objects

diabetes
DatasetInventory.names

next(ds_objects).name

ds = DatasetInventory(name='boston')
ds = DatasetInventory(name='iris')
ds = DatasetInventory(name='digits')
ds = DatasetInventory(name='diabetes')
ds.desc
ds.names
ds.cols
