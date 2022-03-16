# OpsLyft Assignment 1

- [x] Dockerized a flask application and pushed to AWS ECR
- [x] Set up a CI workflow (on this repository) that runs pylint on the python files in this repo on any push 
- [x] Setup a CD workflow to deploy the given image onto ECS on EC2 or fargate
- [x] Bonus: Check if code has secrets in CI pipeline
- [x] Bonus: Configure ECS for auto-scaling and load balancing
- [x] Bonus: CI to check code quality

## Stage 1
*Dockerize a simple Hello World Flask Application which responds with a message that is set up as an environment variable and deploy the docker image to AWS ECR.*

Done using the Dockerfile

## Stage 2
*Develop a CI/CD pipeline(Github Actions/Jenkins or your own choice) which would lint the python code and push the updated image to ECR.*

This repo has pylint CI workflow on Actions for python versions >= 3.8

## Stage 3
*Please create a Github repository with the application code, Dockerfile and the CI/CD workflows.*

*Bonus: ECS could be configured for autoscaling and/or load-balancing. CI pipeline could check the code quality or are there any secrets in the code.*

Workflow defined in aws.yml builds the image and pushes it to ECR repo and deploys onto an ECS service

The deployed container is currently deployed and is running on [18.116.48.65](http://18.116.48.65:5000/)

# Summary
- There are 3 defined workflows
1. Deploy to ECS (triggered on any push to the repo except on readme file) <br /> 
> *builds docker image from root directory, pushes it to ECR and uses the image to deploy on ECS* <br />
2. Pylint (triggered on all pushes that change or create python files) <br />
> *Lints the python code, exits with a non-zero value on any lint score < 10* <br />
3. Check for Secrets (triggered on all pushes that change or create python files, except the code that does the checking for secrets [./check_secrets.py](check_secrets.py)) <br />
> *Code is checked for explicit secrets such as api keys or secrets by the driver code in* [./check_secrets.py](check_secrets.py),rexits with a non zero value if secrets are found.*