import pandas as pd


def load_dataset(set_name: str) -> dict:
    data = pd.read_csv(f"../data/golden/{set_name}_data.csv")
    X = data.drop("target", axis=1)
    y = data["target"]

    return {"features": X, "target": y}
