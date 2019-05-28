import torchvision.datasets as datasets

import os
import shutil


def create_dataset(CIFAR100=False):
    print('Creating dataset')
    imfolder = '/home/gjeanneret/CIFAR10'

    shutil.rmtree(imfolder)
    for i in range(100):
        try:
            os.makedirs(imfolder + '/' + str(i))
        except:
            pass

    if CIFAR100:
        ds = datasets.CIFAR100
    else:
        ds = datasets.CIFAR10

    dataset = ds(
        root='/media/SSD2/dataset', train=True, download=True, transform=None
    )

    for index in range(len(dataset)):
        if (index + 1) % 1000 == 0:
            print(str(index+1) + '/' + str(len(dataset)))
        im, label = dataset.__getitem__(index)
        # PIL im, label
        im.save(imfolder + '/' + str(label) + '/' + str(index) + '.jpg')
    print('')
