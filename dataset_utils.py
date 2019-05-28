from PIL import Image


class dataset_exclude_category_ImageFolder:
    def __init__(self, dataset, cat_exlude=[0]):
        self.len = 1
        self.cat_exlude = cat_exlude
        self.imgs = []
        self.transform = dataset.transform
        self.target_transform = dataset.target_transform
        self._init_dataset(dataset)

    def __len__(self):
        return self.len

    def __getitem__(self, idx):
        path, target = self.imgs[idx]
        sample = self.loader(path)
        if self.transform is not None:
            sample = self.transform(sample)
        if self.target_transform is not None:
            target = self.target_transform(target)

        return sample, target

    def _init_dataset(self, dataset):
        data = dataset.imgs
        self.imgs = [
            i for i in data if i[1] not in self.cat_exlude
        ]
        self.len = len(self.imgs)

    def loader(self, path):
        with open(path, 'rb') as f:
            img = Image.open(f)
            return img.convert('RGB')
