## Test in local
$ node SumService.js

In an other terminal
$ curl -d "6 3" -X POST http://127.0.0.1:50001
==> 9


## deploy app
$ gcloud app deploy sum-app.yaml

test:
$ curl -d "6 3" -X POST [@service]
==> 9
