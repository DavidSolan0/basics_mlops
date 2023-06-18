import os
from src.model.model_training import train_model
from src.model_tracking.utils import create_experiment_id

# Define test variables
model_name = "test"
experiment_id = create_experiment_id(model_name)


def test_model_training():
    train_model(model_name=model_name, experiment_id=experiment_id)

    expected_path = f"mlruns/{experiment_id}"
    assert os.path.exists(expected_path)

    # Delete folder
    os.rmdir(expected_path)
    print(f"Experiment '{experiment_id}' has been deleted.")
