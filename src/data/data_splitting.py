import os
import pandas as pd
from sklearn.model_selection import train_test_split


from data.utils import create_path


def split_data(input_dir, model_name, output_dir, test_size):
    # Load the data
    input_path = os.path.join("data", model_name, input_dir)
    input_file = create_path(folder=input_path, name="preprocessed")
    data = pd.read_csv(input_file)

    # Split the data into train, test, and validation sets
    train_data, test_data = train_test_split(data, test_size=test_size, random_state=42)
    test_data, valid_data = train_test_split(test_data, test_size=0.5, random_state=42)

    # Create the output directory if it doesn't exist
    output_path = os.path.join("data", model_name, output_dir)
    os.makedirs(output_path, exist_ok=True)
    print(f"Splitting Output path:", output_path)

    # Save the split data as CSV in the output directory
    train_path = create_path(folder=output_path, name="train")
    test_path = create_path(folder=output_path, name="test")
    valid_path = create_path(folder=output_path, name="valid")

    train_data.to_csv(train_path, index=False)
    test_data.to_csv(test_path, index=False)
    valid_data.to_csv(valid_path, index=False)
