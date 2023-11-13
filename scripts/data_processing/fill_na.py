import sys
import os
import pandas as pd

if len(sys.argv) !=2:
    sys.stderr.write("Arguments error. Usage: \n")
    sys.stderr.write("\tpython fill_na.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("data", "stage2", "train.csv")
os.makedirs(os.path.join("data", "stage2"), exist_ok=True)

df = pd.read_csv(f_input)

df["box_office"].fillna(df["box_office"].mean(), inplace= True)
df["runtime"].fillna(df["runtime"].mean(), inplace= True)
df["rating_MPAA"].fillna(0, inplace= True)

df.to_csv(f_output, index=False)

