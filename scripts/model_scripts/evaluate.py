import sys
import os
import pickle
import json

from dvclive import Live
import pandas as pd
from sklearn.metrics import f1_score as f1
from sklearn.metrics import accuracy_score as acc


if len(sys.argv) !=3:
    sys.stderr.write("Arguments error. Usage: \n")
    sys.stderr.write("\tpython evaluate.py data-file\n")
    sys.exit(1)

with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

f_input = os.path.join("data/stage4/test.csv")
test = pd.read_csv(f_input)

X_test = test.drop(columns = "fresh").values
y_test = test["fresh"].values

y_predict=model.predict(X_test)

Acc = acc(y_predict,y_test)
F1 =  f1(y_predict,y_test,average="binary")

with Live("evaluate", dvcyaml=False) as live:
    if not live.summary:
        live.summary = {"Acc": {}, "F1": {}}
    live.summary["Acc"] = Acc
    live.summary["F1"] = F1

