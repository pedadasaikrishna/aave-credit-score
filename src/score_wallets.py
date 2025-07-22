import json
import pandas as pd
from feature_engineering import engineer_features
from model import train_and_score

def load_data(json_file):
    with open(json_file) as f:
        data = json.load(f)
    return pd.DataFrame(data)

def main():
    import os
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "../data/user-wallet-transactions.json")
    df = load_data(json_path)

    features_df = engineer_features(df)
    result = train_and_score(features_df)
    result.to_csv("wallet_scores.csv", index=False)
    print("✅ Scoring complete. Output written to wallet_scores.csv")

if __name__ == "__main__":
    main()
