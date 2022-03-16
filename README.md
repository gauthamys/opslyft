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


The deployed container is currently deployed and is running on [18.188.189.91](http://18.188.189.91:5000/)
