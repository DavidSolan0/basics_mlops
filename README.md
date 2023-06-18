# MLops-Basics
This repo contains the code, images, and documentation to run a basic MLOps pipeline.

# UML Component diagram
To have a better understanding I propose the following component diagram which depicts the components envolve in the CI and CT pipelines.

![image](https://github.com/DavidSolan0/mlops-repository/assets/80591909/79a45949-b41e-4fe8-9f1e-9dcb5864178a)

The components and the packages of components depicted in the previous image are the ones to be tested through the unit and integrate tests before any commit would be merged into the master branch. This would help us to avoid merging untested changes and crashing the workflow. Specifically I'm to test the following point of the workflow depicted in the image.

1. In the data collection the versioned artifacts are created.
2. In the data preprocessing the versioned artifacts are created.
3. The model training doesn't overfit and returns the expected artifacts (e.g., confusion matrix, scores, metrics, and so on.)
4. The workflow logic works properly.
5. The model registry creates the new model version artifacts when corresponding. [PENDING]
6. The model publishing creates the model artifacts in the production enviroment. [PENDING]
7. Data drift and concept drift triggers the CT when corresponding. [PENDING]

## Project Excecution
### Virtual Enrivoment
Create a conda environment by running
```
python -m venv venv
```
Then, activate the environment
```
source venv/Scripts/activate
```
and install the dependencies
```
pip install -r requirements.txt
```
### Running the project

To run the project, run
```
python src/main.py --model_name NAME --num_instances NUM_INSTANCES
```
Once it's done you will have the following project structure:

![image](https://github.com/DavidSolan0/basics_mlops/assets/80591909/a7716f2b-2990-45b6-8011-96ac421e9658)

### Model Tracking
To see your experiments and runs with MLFlow, run 
```
mlflow ui
```

This will launch you to your browse to see the following dashboard.

![image](https://github.com/DavidSolan0/basics_mlops/assets/80591909/69cba549-d97a-44a1-89e6-43b1d7fb1c60)

You'll be able to view your excecutions, track metrics and save artifacts to run inference. 

![image](https://github.com/DavidSolan0/basics_mlops/assets/80591909/75cae4ec-a66c-4a94-9e9b-fed9b4c5e24a)

## FUTURE WORK

* Data versioning with DVC and AWS S3. 
* Model tracking with MLFlow and AWS S3.
* Scalability improvements working in a AWS EC2 instance instead of a local workspace.
