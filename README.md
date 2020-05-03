# Google-app-engine-samples

## LINUX ENVIRONMENT

### Components to install in your Linux

python >=3.0

node >= 8.10.0

curl >= 7.58.0

npm >= 3.5.2

### Gcloud versions:

Google Cloud SDK 290.0.1

app-engine-python 1.9.90

bq 2.0.56

cloud-datastore-emulator 2.1.0

core 2020.04.24

gsutil 4.49


### See documentation GOOGLE:
https://cloud.google.com/appengine/docs/standard/python3/quickstart

## Explanations

First, you have to create a google account

### Download SDK
https://cloud.google.com/sdk/docs

### Update components
$ gcloud components update

### Create a project
$ gcloud projects create [YOUR_PROJECT_ID] --set-as-default

### Check if the project was created
$ gcloud projects describe [YOUR_PROJECT_ID]

### Create App Engine
$ gcloud app create --project=[YOUR_PROJECT_ID]

### Activate bill and Cloud Build
go to https://console.cloud.google.com

Select your project

Click on bill and follow the procedure

Go back to the main page of your project

Select API and services

Research Cloud Build

Click on activate

## Deploy samples 
Each folders have a README to deploy applications

### Calculator
Sample of a calculator which communicate (http requests) with nodes. You need to deploy all nodes before

install App Engine or python3:

$ gcloud components install app-engine-python

### Helloword
sample example helloworld with nodesJS 

### env
Environment created for python

### NodeJS
Contains all nodes for calculator (Sum, Sub, Mul and Div)

### test.py
Test nodes in Python: Sum Sub Mul and Div
To test yours change URLs at the begining of test.py
then:

$ python test.py

You can test each node with curl (Look README of each nodes to see the command line)
