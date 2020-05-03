## Test in local
$ node DivService.js

In an other terminal
$ curl -d "6 3" -X POST http://127.0.0.1:50004
==> 2


## deploy app
$ gcloud app deploy div-app.yaml

test:
$ curl -d "6 3" -X POST [@service]
==> 2
