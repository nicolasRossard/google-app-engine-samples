## Create Environment Python

### Create Python environment
$ python3 -m venv [name-env]

$ source [name-env]/bin/activate
==> (name-env) $

### To deactivate environment
(name-env) $ dactivate

## Test in local:

### Install modules:
(env) $ pip install -r requirements.txt

### Test
(env) $ python main.py

See in http://localhost:8080/

## DEPLOY APP ENGINE 
Do README for application before then:

### Deploy App Engine
$ gcloup app deploy 

### To verify:
$ gcloud app browse
