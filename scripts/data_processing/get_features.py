import sys
import os
import pandas as pd

if len(sys.argv) !=2:
    sys.stderr.write("Arguments error. Usage: \n")
    sys.stderr.write("\tpython get_features.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("data", "stage1", "train.csv")
os.makedirs(os.path.join("data", "stage1"), exist_ok=True)

df = pd.read_csv(f_input)

df = df.drop(columns = ["synopsis", "genre", "director", "writer", "theater_date", "dvd_date", "studio", "dvd_date_int", "theater_date_int", "review", "critic", "publisher","date", "rating_10"])

df.to_csv(f_output, index = False)
