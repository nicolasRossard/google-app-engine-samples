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

### Deploy samples 
Now you can go in the folders and deploy all samples

If you need to deploy Python3 App Engine install components for Python:
$ gcloud components install app-engine-python

### Calculator
Sample of a calculator which communicate (http request) with nodesJS
You need to deploy all nodeJS before

### Helloword
sample example helloworld with nodesJS 

### env
Environment created for python

### test.py
Test my services: Sum Sub Mul and Div
To test yours change URLs at the begining of test.py
then:

$ python test.py
