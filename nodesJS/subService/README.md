## Test in local
$ node SubService.js

In an other terminal
$ curl -d "6 3" -X POST http://127.0.0.1:50002
==> 3


## deploy app
$ gcloud app deploy sub-app.yaml

test:
$ curl -d "6 3" -X POST [@service]
==> 3
