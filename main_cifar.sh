# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
#!/bin/bash

ARCH="alexnetc"
LR=0.05
WD=-5
K=1000
WORKERS=12
EXP=/home/gjeanneret/UNSUPERVISED/deepcluster_exclude

mkdir -p ${EXP}

# CUDA_VISIBLE_DEVICES=2 python main_cifar.py --exp ${EXP} --arch ${ARCH} \
#   --lr ${LR} --wd ${WD} --k ${K} --sobel --verbose --workers ${WORKERS} \
#   --batch 5000

CUDA_VISIBLE_DEVICES=3 python main_cifar.py --exp ${EXP} --arch ${ARCH} \
  --lr ${LR} --wd ${WD} --k ${K} --verbose --workers ${WORKERS} \
  --batch 5000 --exclude --sobel