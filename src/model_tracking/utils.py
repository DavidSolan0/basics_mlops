import mlflow


def create_experiment_id(experiment_name):
    experiment = mlflow.get_experiment_by_name(experiment_name)
    if not experiment:
        experiment_id = mlflow.create_experiment(experiment_name)
        return experiment_id
    else:
        return experiment.experiment_id
