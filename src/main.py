import argparse
from etl import etl
from model.model_training import train_model


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data Collection")
    parser.add_argument(
        "--num_instances",
        type=int,
        required=True,
        help="Number of instances for data generation",
    )
    parser.add_argument("--test_size", type=float, required=True, help="Test set size")
    args = parser.parse_args()

    print("Starting etl")
    etl(num_instances=args.num_instances, test_size=args.test_size)

    print("Starting model training")
    train_model()
