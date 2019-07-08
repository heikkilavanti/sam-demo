# SAM Demo

Small demo project to try and understand how a "microservice" API could potentially look like with AWS Lambda and SAM.

Content:

* ``table/``: folder containing code required to create and delete the DynamoDB table (just for simplicity...)
* ``task/``: folder containing code to create, get and delete tasks
* ``tests/``: folder containing integration (robot) tests to verify that code is working. Should also add unit tests
* ``template.yaml``: the SAM template that sets up the API GW and Lamda environment

## Requirements

* [AWS account](https://aws.amazon.com/console/)
* [DockerHub account](https://hub.docker.com/)
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html), for Mac use homebrew: ```brew install awscli```
* [Python 3 installed](https://www.python.org/downloads/)
* virtualenv installed: `python3 -m venv /path/to/new/virtual/environment`
* [Docker installed](https://www.docker.com/community-edition)

## Setup process

Setup AWS CLI with account info (if not yet done)

```bash
aws configure
```

### Local development

**Dowload DynamoDB docker image**
```bash
docker pull amazon/dynamodb-local
```

Create Docker network
```bash
docker network create sam-demo
```

Start DynamoDB container in detached mode, attach to Docker network
```bash
docker run -d -p 8000:8000 --network sam-demo --name dynamodb amazon/dynamodb-local
```

Navigate to `sam_demo` folder, activate virtualenv and install requirements
```bash
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```

To test with remote DynamoDB, start local Lambda and API GW via SAM CLI, attach to Docker network
```bash
sam local start-api
```

To test with local DynamoDB Lambda and API GW via SAM CLI, attach to Docker network
```bash
sam local start-api --docker-network sam-demo --
```

Run Robot tests to verify API functionality
```bash
robot --exitonfailure --critical critical tests/robot/api_tests.robot
```

##TODO

1. Add more unit tests
2. Add instructions on deploying to AWS
