AWS EC2 API
===========

This API can be used to spawn the new EC2 instance or to delete the EC2 instance.


## HTTP Methods:

* POST `\create`

    Request:

    `application/json`

    ```
    {
        "username": "suitepad",
        "password": "suitepad"
    }
    ```

    Response:

    ```
    {
        "ip": <some-ip>,
        "status": <status>
    }
    ```
    Description: Spawn EC2 instance in sync way


* POST `\create-async`

    Request:

    `application/json`
    ```
    {
        "username": "suitepad",
        "password": "suitepad"
    }
    ```

    Response:

    ```
    {
        "task_id": <uuid>,
        "message": <message>
    }
    ```

    Description: Spawn EC2 instance in async way


* GET `/status/<id>`

    Response:

    ```
    {
        "ip": <some-ip>,
        "status": <status>
    }
    ```

    Description: Get the detail of the task by task id


* GET `/delete/<ip>`

    Response:

    ```
    {
        "ip": <some-ip>,
        "status": <status>
    }
    ```

    Description: Delete the EC2 instance by IP in sync manner


* GET `/delete-async/<ip>`

    Response:

    ```
    {
        "task_id": <uuid>,
        "message": <message>
    }
    ```

    Description: Delete the EC2 instance by IP in async manner


### Tech Stack

* Flask
* Celery
* Ansible
* AWS CLI


### Steps to Run

* Install AWS CLI and configure it. Please note that the response should be JSON.

    ```
    pip install awscli
     ```
    ```
    aws configure
    ```

* Install and configure ansible

    ```
    pip install ansible
    ```

* Install all dependencies by

    ```
    pip install -r requirements.txt
    ```

* Run async task manager by

    ```
    celery -A tasks worker --loglevel=info
    ```

* Run the server by

    ```
    python api.py
    ```

* Start firing API on host http://0.0.0.0:5000


### Details

* The API creates `t2.micro` instance on AWS with CentOS 6.7
* The reason to use AWS EC2 public IP not private IP, because we need VPN from AWS
to our local network.
* The reason to go with Ansible is, every module in ansible is idempotent, so you
can safely run same process again and again.
* The demo video is shared with you.
