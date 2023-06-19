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
5. The model registry creates the new model version artifacts when corresponding. [PENDING]
6. The model publishing creates the model artifacts in the production environment. [PENDING]
7. Data drift and concept drift trigger the CT when corresponding. [PENDING]

## Project Execution
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

This will launch you to your browser to see the following dashboard.

![image](https://github.com/DavidSolan0/basics_mlops/assets/80591909/69cba549-d97a-44a1-89e6-43b1d7fb1c60)

You'll be able to view your executions, track metrics, and save artifacts to run inference. 

![image](https://github.com/DavidSolan0/basics_mlops/assets/80591909/75cae4ec-a66c-4a94-9e9b-fed9b4c5e24a)

## FUTURE WORK

* Data versioning with DVC and AWS S3. 
* Model registry and tracking with MLFlow and AWS S3.
* Scalability improvements working in an AWS EC2 instance instead of a local workspace.

### Data versioning with DVC

DVC will create a cache tracking with GitHub to identify the code changes that imply data modifications. We can link a remote with AWS S3 where the files will be stored to share across teams. Thus we avoid loading large files into GitHub but are still able to find the desired versions to run tests and compare models and code versions.

To get an idea of what would be the expected result I created a remote with DVC in Google Drive [here](https://github.com/DavidSolan0/basics_mlops/blob/mlops-project-requirement/data.dvc) you have the cache file how it would look like and [here](https://github.com/DavidSolan0/basics_mlops/blob/mlops-project-requirement/.dvc/config) the remote configuration. For more details please follow this [link](https://dvc.org/doc/start/data-management/data-versioning?tab=Windows-Cmd-)

### Model Registry and Tracking

The idea is to create a pipeline that allows to reproduce the MLFlow experiments and based on statistical hypothesis systems or bootstrap procedures define if a new run should be registered as a new model version into production. The model artifacts folder then can be uploaded into an S3 bucket in AWS to share across teams and execute remotely. 

