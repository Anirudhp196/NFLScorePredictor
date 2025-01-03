import pandas as pd
import numpy as np;

RAW_DATA_PATH = "NFLData/scores.csv"

df = pd.read_csv(RAW_DATA_PATH)
##print(df);

important_columns = ["team_home", "score_home", "score_away", "team_away"]
df = df[important_columns]
print(df);

def save_data(df, file_path):
    if df is not None:
        df.to_csv(file_path, index=False)
        print(f"Cleaned data saved to {file_path}")
    else:
        print("No data to save.")

def main():
    save_data(df, "NFLData/cleaned_nfl_scores.csv")

if __name__ == "__main__":
    main()