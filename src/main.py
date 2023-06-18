import argparse
from etl import etl
from model.model_training import train_model
from model_tracking.utils import create_experiment_id


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data Collection")
    parser.add_argument("--model_name", type=str, default="iris", help="Model name")
    parser.add_argument(
        "--num_instances",
        type=int,
        required=True,
        help="Number of instances for data generation",
    )
    parser.add_argument("--test_size", type=float, default=0.2, help="Test set size")
    args = parser.parse_args()

    # Data Preprocessing
    print("Starting etl")
    etl(
        num_instances=args.num_instances,
        model_name=args.model_name,
        test_size=args.test_size,
    )

    # Get experiment id
    experiment_id = create_experiment_id(args.model_name)

    # Training
    print("Starting model training")
    train_model(args.model_name, experiment_id)
