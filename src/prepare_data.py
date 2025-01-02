import pandas as pd
import numpy as np;

RAW_DATA_PATH = "NFLData/scores.csv"

df = pd.read_csv(RAW_DATA_PATH)
print(df);
