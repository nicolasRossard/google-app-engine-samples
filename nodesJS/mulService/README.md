## Test in local
$ node MulService.js

In an other terminal
$ curl -d "6 3" -X POST http://127.0.0.1:50003
==> 18


## deploy app
$ gcloud app deploy mul-app.yaml

test:
$ curl -d "6 3" -X POST [@service]
==> 18
