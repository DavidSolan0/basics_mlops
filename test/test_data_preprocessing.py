import os
import pandas as pd

from src.data.utils import create_path
from src.data.data_preprocessing import preprocess_data

# Define test variables
input_dir = "bronze"
output_dir = "silver"
model_name = "test"


# Define test function
def test_preprocess_data():
    # Call the function to preprocess the data
    preprocess_data(input_dir=input_dir, model_name=model_name, output_dir=output_dir)

    # Assert that output directory was created
    output_path = os.path.join("data", model_name, output_dir)
    assert os.path.exists(output_path)

    # Assert that the values in the preprocessed data are between 0 and 1
    output_file = create_path(folder=output_path, name="preprocessed")
    data = pd.read_csv(output_file)

    data.drop(columns=["target"], inplace=True)
    assert all(data.min() >= 0) and all(data.max() <= 1)
