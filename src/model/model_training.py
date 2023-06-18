import mlflow
import mlflow.sklearn
import numpy as np
from hyperopt import hp, tpe, Trials, fmin
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from model.utils import load_dataset


def train_model():
    # Load the train data from the "golden" folder
    train_dict = load_dataset("train")
    X_train = train_dict["features"]
    y_train = train_dict["target"]

    # Load the test data from the "golden" folder
    test_dict = load_dataset("test")
    X_test = test_dict["features"]
    y_test = test_dict["target"]

    # Load the valid data from the "golden" folder
    valid_dict = load_dataset("valid")
    X_valid = valid_dict["features"]
    y_valid = valid_dict["target"]

    # Define the hyperparameter search space
    hyperparameter_space = {
        "C": hp.loguniform("C", np.log(0.01), np.log(10.0)),
        "penalty": hp.choice("penalty", ["l2", "elasticnet"]),
    }

    # Define the objective function for hyperparameter optimization
    def objective(hyperparameters):
        model = LogisticRegression(**hyperparameters)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_valid)
        accuracy = accuracy_score(y_valid, y_pred)
        return -accuracy  # Minimize the negative accuracy

    # Perform hyperparameter optimization
    best_hyperparameters = fmin(
        objective,
        hyperparameter_space,
        algo=tpe.suggest,
        max_evals=100,
    )

    # Retrieve the best hyperparameters
    best_hyperparameters = {**best_hyperparameters, "solver": "lbfgs"}

    # Train the model with the best hyperparameters
    model = LogisticRegression(**best_hyperparameters)
    model.fit(X_train, y_train)

    # Log the model and its metrics using MLflow
    with mlflow.start_run():
        mlflow.log_params(best_hyperparameters)

        # Evaluate on train data
        train_predictions = model.predict(X_train)
        train_accuracy = accuracy_score(y_train, train_predictions)
        mlflow.log_metric("train_accuracy", train_accuracy)

        # Evaluate on test data
        test_predictions = model.predict(X_test)
        test_accuracy = accuracy_score(y_test, test_predictions)
        mlflow.log_metric("test_accuracy", test_accuracy)

        # Save the model artifacts
        mlflow.sklearn.log_model(model, "model_artifacts")
