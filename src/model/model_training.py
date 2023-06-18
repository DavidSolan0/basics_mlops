import mlflow
import mlflow.sklearn
import numpy as np
from joblib import load
from hyperopt import hp, tpe, Trials, fmin
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score

from model.utils import load_dataset


def train_model(model_name, experiment_id):
    # Load the train data from the "golden" folder
    train_dict = load_dataset(model_name, "train")
    X_train = train_dict["features"]
    y_train = train_dict["target"]

    # Load the test data from the "golden" folder
    test_dict = load_dataset(model_name, "test")
    X_test = test_dict["features"]
    y_test = test_dict["target"]

    # Load the valid data from the "golden" folder
    valid_dict = load_dataset(model_name, "valid")
    X_valid = valid_dict["features"]
    y_valid = valid_dict["target"]

    # Load scaler for inference
    scaler_path = f"data/{model_name}/silver/scaler.pickle"

    # Define the hyperparameter search space
    hyperparameter_space = {
        "alpha": hp.loguniform("alpha", np.log(0.0001), np.log(1.0)),
    }

    # Define the objective function for hyperparameter optimization
    def objective(hyperparameters):
        model = SGDClassifier(
            **hyperparameters, penalty="elasticnet", loss="modified_huber"
        )
        model.fit(X_train, y_train)
        y_pred = model.predict(X_valid)
        accuracy = accuracy_score(y_valid, y_pred)
        return -accuracy  # Minimize the negative accuracy

    # Perform hyperparameter optimization
    trials = Trials()
    best_hyperparameters = fmin(
        objective, hyperparameter_space, algo=tpe.suggest, max_evals=10, trials=trials
    )

    # Retrieve the best hyperparameters
    best_hyperparameters = {
        **best_hyperparameters,
        "penalty": "elasticnet",
        "loss": "modified_huber",
    }

    # Train the model with the best hyperparameters
    model = SGDClassifier(**best_hyperparameters)
    model.fit(X_train, y_train)

    # Set the experiment path for saving the runs
    mlflow.set_experiment(experiment_id=experiment_id)

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
        mlflow.log_artifact(scaler_path)
