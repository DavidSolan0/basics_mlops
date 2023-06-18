import os
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.utils import shuffle


from data.utils import create_path


def collect_data(num_instances, output_dir):
    # Load the famous iris dataset
    iris = load_iris()
    data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    data["target"] = iris.target

    # Shuffle the dataset randomly
    data = shuffle(data, random_state=42)

    # Take a subset of instances based on the specified number
    data = data.iloc[:num_instances]

    # Create the output directory if it doesn't exist
    output_path = os.path.join("data", output_dir)
    os.makedirs(output_path, exist_ok=True)
    print(f"Collection Output path:", output_path)

    # Save the raw data as CSV in the output directory
    output_file = create_path(folder=output_path, name="raw")
    print(f"Collection Output file:", output_file)
    data.to_csv(output_file, index=False)
