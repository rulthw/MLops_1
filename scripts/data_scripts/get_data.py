#!/usr/bin/python3

from catboost.datasets import rotten_tomatoes

train, test = rotten_tomatoes()

train.to_csv("~/MLops_1/data/raw/train.csv", columns=train.columns)

test.to_csv("~/MLops_1/data/raw/test.csv", columns=test.columns)
