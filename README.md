[![MLflow CI/CD Pipeline](https://github.com/DavidSolan0/basics_mlops/actions/workflows/main.yml/badge.svg)](https://github.com/DavidSolan0/basics_mlops/actions/workflows/main.yml)

# MLops-Basics
This repo contains the code, images, and documentation to run a basic MLOps pipeline.

# UML Component diagram
To have a better understanding I propose the following component diagram which depicts the components involved in the CI and CT pipelines.

![image](https://github.com/DavidSolan0/mlops-repository/assets/80591909/79a45949-b41e-4fe8-9f1e-9dcb5864178a)

The components and the packages of components depicted in the previous image are the ones to be tested through the unit and integrate tests before any commit would be merged into the master branch. This would help us to avoid merging untested changes and crashing the workflow. Specifically, I'm to test the following point of the workflow depicted in the image.

1. In the data collection the versioned artifacts are created.
2. In the data preprocessing the versioned artifacts are created.
3. The model training doesn't overfit and returns the expected artifacts (e.g., confusion matrix, scores, metrics, and so on.)
4. The workflow logic works properly.
5. The model registry creates the new model version artifacts when corresponding.
6. The model publishing creates the model artifacts in the production environment.
7. Data drift and concept drift trigger the CT when corresponding.
