import os
import pandas as pd
from joblib import dump
from sklearn.preprocessing import MinMaxScaler

from data.utils import create_path


def preprocess_data(input_dir, model_name, output_dir):
    # Load the raw data
    input_path = os.path.join("data", model_name, input_dir)
    input_file = create_path(folder=input_path, name="raw")
    data = pd.read_csv(input_file)

    # Perform data preprocessing (scaling)
    scaler = MinMaxScaler()

    features = data.drop("target", axis=1)
    target = data["target"]

    # Fit the scaler on the features data
    scaler.fit(features)

    # Transform the features using the scaler
    scaled_features = scaler.transform(features)

    # Create a new DataFrame with the scaled features
    data_scaled = pd.DataFrame(scaled_features, columns=features.columns)

    # Concatenate the scaled features DataFrame with the target column
    data_scaled["target"] = target

    # Create the output directory if it doesn't exist
    output_path = os.path.join("data", model_name, output_dir)
    os.makedirs(output_path, exist_ok=True)
    print(f"Preprocessing Output path:", output_path)

    # Save the preprocessed data as CSV in the output directory
    output_file = create_path(folder=output_path, name="preprocessed")
    print(f"Preprocessing Output file:", output_file)
    data_scaled.to_csv(output_file, index=False)

    # Save scaler
    scaler_path = os.path.join(output_path, "scaler.pickle")
    dump(scaler, scaler_path)
