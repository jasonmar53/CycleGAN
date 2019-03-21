#!/bin/bash
# https://github.com/junyanz/CycleGAN/blob/master/datasets/download_dataset.sh

URL1=http://imagenet.stanford.edu/internal/car196/cars_train.tgz
URL2=http://imagenet.stanford.edu/internal/car196/cars_test.tgz
ZIP_FILE=./data/cars_train.tgz
ZIP_FILE2=./data/cars_test.tgz
TARGET_DIR=./data/stanford-cars-dataset/
wget -N $URL1 -O $ZIP_FILE
wget -N $URL2 -O $ZIP_FILE2
mkdir -p $TARGET_DIR
tar xvzf $ZIP_FILE -d
tar xvzf $ZIP_FILE2 -d

