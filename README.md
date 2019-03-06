# HouseKeeping

The API as python based. The APis ae built on Flask framework and use mysql as their database. 

## Install

    pip install -r requirements.txt

## Run the app

    flask run

# REST API

The REST API to the example app is described below.

## Add an asset

### Request

`POST /add_asset/`

    curl -X POST https://udaantest.herokuapp.com/add_asset -H 'Content-Type: application/json' \ -H 'content-type: multipart/form-data -F assetID=<string>

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    "The asset is sucessfuly added"
## Add an task

### Request

`POST /add_task/`

    curl -X POST https://udaantest.herokuapp.com/add_task -H 'Content-Type: application/json' \ -H 'content-type: multipart/form-data -F taskID=<string> -F frequency=<string>

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    "The task is sucessfuly added"

## Add an worker

### Request

`POST /add_worker/`

    curl -X POST https://udaantest.herokuapp.com/add_worker -H 'Content-Type: application/json' \ -H 'content-type: multipart/form-data -F workerID=<string>

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    "The worker is sucessfuly added"
## Fetch details of all assets

### Request

`GET /assets/all`

    curl -X GET https://udaantest.herokuapp.com/assets/all -H 'Content-Type: application/json' 

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    {answer:[array of asset objects]}
## Fetch details of a specific worker with giver workerID

### Request

`GET /get_tasks_for_workers/<workerID>`

    curl -X GET https://udaantest.herokuapp.com/get_tasks_for_workers/<workerID> -H 'Content-Type:application/json'  

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    {answer:[required Object]}

## Allocate the tak to a worker

### Request

`GET /allocate_task

    curl -X POST http://localhost:5000/allocate_task -H 'Content-Type: application/json' -F assetID=<String> -F workerID=<String> -F taskID=<String> -F timeOfAllocation=<TimeStamp> -F taskTobePerformedBy=<TimeStamp> 

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    "The task is successfuly alloted"

_*All tiemstamps must be provided in the given format **%Y-%m-%d %H:%M:%S**.*_

_*The information about the frequency was inadequate. This means I could only allot a worker to the a task but cannot check when the worker is free or not.*_

_*I have used formdata to pass data to the API. So to evaluate the work, please use POST. It has a special input type where we an pass the parameters via formdata*_

_*Database used is mySQL. The mySQL server is provided by remotemysql.com*_