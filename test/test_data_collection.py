import os
import pandas as pd
from src.data.utils import create_path
from src.data.data_collection import collect_data

# Define test variables
num_instances = 20
output_dir = "bronze"
model_name = "test"


def test_collect_data():
    collect_data(num_instances, model_name, output_dir)

    output_path = os.path.join("data", model_name, output_dir)
    raw_file = create_path(folder=output_path, name="raw")
    print(raw_file)
    assert os.path.exists(raw_file)

    data = pd.read_csv(raw_file)
    assert len(data) == num_instances
