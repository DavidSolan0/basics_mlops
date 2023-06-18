import os
from src.data.data_splitting import split_data

# Define test variables
input_dir = "silver"
output_dir = "golden"
test_size = 0.2
model_name = "test"


# Define test function
def test_split_data():
    # Call the function to split the test data
    split_data(
        model_name=model_name,
        input_dir=input_dir,
        output_dir=output_dir,
        test_size=test_size,
    )

    # Assert that output directory was created
    output_path = os.path.join("data", model_name, output_dir)
    assert os.path.exists(output_path)

    # Assert that there are three files with names
    # train, test, valid
    file_names = os.listdir(output_path)
    assert len(file_names) == 3
