from data.data_collection import collect_data
from data.data_preprocessing import preprocess_data
from data.data_splitting import split_data


def etl(model_name, num_instances: int, test_size: float):
    collect_data(
        model_name=model_name, num_instances=num_instances, output_dir="bronze"
    )
    preprocess_data(model_name=model_name, input_dir="bronze", output_dir="silver")
    split_data(
        model_name=model_name,
        input_dir="silver",
        output_dir="golden",
        test_size=test_size,
    )
