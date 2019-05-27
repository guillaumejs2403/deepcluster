import torch
import torchvision.datasets as datasets

import os
import pdb
import shutil
from PIL import Image


imfolder = '/home/gjeanneret/CIFAR10'

shutil.rmtree(imfolder)
for i in range(100):
    try:
        os.makedirs(imfolder + '/' + str(i))
    except:
        pass


dataset = datasets.CIFAR100(root = '/media/SSD2/dataset',train = True, download = True, transform=None)


for index in range(len(dataset)):
    print(str(index+1) + '/' + str(len(dataset)))
    im, label = dataset.__getitem__(index)
    #PIL im, label
    im.save(imfolder + '/' + str(label) + '/' + str(index) + '.jpg')
print('')