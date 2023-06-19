import os
import shutil
import pandas as pd
from src.data.utils import create_path
from src.data.data_collection import collect_data
from src.data.data_preprocessing import preprocess_data
from src.data.data_splitting import split_data
from src.model.model_training import train_model
from src.model_tracking.utils import create_experiment_id


class CICDTest:
    def __init__(self, model_name):
        self.model_name = model_name

    def test_collect_data(self, num_instances, output_dir):
        collect_data(num_instances, model_name=self.model_name, output_dir=output_dir)

        output_path = os.path.join("data", self.model_name, output_dir)
        raw_file = create_path(folder=output_path, name="raw")
        print(raw_file)
        assert os.path.exists(raw_file)

        data = pd.read_csv(raw_file)
        assert len(data) == num_instances

    def test_preprocess_data(self, input_dir, output_dir):
        preprocess_data(
            input_dir=input_dir, model_name=self.model_name, output_dir=output_dir
        )

        output_path = os.path.join("data", self.model_name, output_dir)
        assert os.path.exists(output_path)

        output_file = create_path(folder=output_path, name="preprocessed")
        data = pd.read_csv(output_file)

        data.drop(columns=["target"], inplace=True)
        assert all(data.min() >= 0) and all(data.max() <= 1)

    def test_split_data(self, input_dir, output_dir, test_size):
        split_data(
            model_name=self.model_name,
            input_dir=input_dir,
            output_dir=output_dir,
            test_size=test_size,
        )

        output_path = os.path.join("data", self.model_name, output_dir)
        assert os.path.exists(output_path)

        file_names = os.listdir(output_path)
        assert len(file_names) == 3

    def test_model_training(self):
        experiment_id = create_experiment_id(self.model_name)
        train_model(model_name=self.model_name, experiment_id=experiment_id)

        expected_path = f"mlruns/{experiment_id}"
        assert os.path.exists(expected_path)

        shutil.rmtree(expected_path)
        print(f"Experiment '{experiment_id}' has been deleted.")


test = CICDTest(model_name="test")
test.test_collect_data(num_instances=30, output_dir="bronze")
test.test_preprocess_data(input_dir="bronze", output_dir="silver")
test.test_split_data(input_dir="silver", output_dir="golden", test_size=0.2)
test.test_model_training()
