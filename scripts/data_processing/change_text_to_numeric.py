import sys
import os
import pandas as pd

if len(sys.argv) !=2:
    sys.stderr.write("Arguments error. Usage: \n")
    sys.stderr.write("\tpython change_text_to_numeric.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("data", "stage3", "train.csv")
os.makedirs(os.path.join("data", "stage3"), exist_ok=True)

df = pd.read_csv(f_input)

df['rating_MPAA'] = df['rating_MPAA'].replace({'R': 1, 'PG-13': 2, 'PG': 3, 'NR': 4, 'G': 5})
df['fresh'] = df['fresh'].replace({'fresh': 1, 'rotten': 0})

df.to_csv(f_output, index=False)




