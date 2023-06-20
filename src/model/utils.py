import pandas as pd


def load_dataset(model_name, set_name: str) -> dict:
    data = pd.read_csv(f"data/{model_name}/golden/{set_name}_data.csv")
    X = data.drop("target", axis=1)
    y = data["target"]

    return {"features": X, "target": y}
