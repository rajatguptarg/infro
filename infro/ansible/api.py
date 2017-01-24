#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flake8: noqa
import json
from flask import Flask, request, jsonify
from tasks import create_ec2_instance, async_create_ec2_instance
from tasks import delete_ec2, async_delete_ec2
from celery.result import AsyncResult


api = Flask(__name__)


INVALID_REQUEST_PARAMS = {
    "error": "Please specify all the parameters."
}

EMPTY_RESPONSE = {
    "message": "Your request is under processing."
}


def make_wait_response(result):
    """
    Returns the response for async tasks
    """
    return {
        "task_id": result,
        "message": "Your request has been intiated. It will take 4-5 \
        minutes to procees. Use task id for future reference."
    }


def get_result_from_task_id(func, task_id):
    """
    Returns the result of sync task from task id
    """
    result = func.AsyncResult(task_id)
    if result.state == 'SUCCESS':
        return result.get(), result.state
    return 'Not Applicable', result.state


def make_result_response(result, status='SUCCESS'):
    """
    Returns response for result of the requests
    """
    return {
        "status": status,
        "ip": result
    }


@api.route('/create-async', methods=['POST'])
def create_ec2_async():
    """
    Web handler to create EC2 instance in async manner
    """
    request_body = request.get_json()
    result = EMPTY_RESPONSE
    try:
        username = request_body['username']
        password = request_body['password']
        ans = async_create_ec2_instance.delay(username, password).task_id
        result = make_wait_response(ans)
    except:
        result = INVALID_REQUEST_PARAMS
    return jsonify(result)


@api.route('/create', methods=['POST'])
def create_ec2_sync():
    """
    Web handler to create EC2 instance in sync manner
    """
    request_body = request.get_json()
    result = EMPTY_RESPONSE
    try:
        username = request_body['username']
        password = request_body['password']
        ans = create_ec2_instance(username, password)
        result = make_result_response(ans)
    except:
        result = INVALID_REQUEST_PARAMS
    return jsonify(result)


@api.route('/delete-async/<ip>', methods=['GET'])
def delete_ec2_async(ip):
    """
    Web handler to delete instance in async manner
    """
    result = EMPTY_RESPONSE
    try:
        ans = async_delete_ec2.delay(ip).task_id
        result = make_wait_response(ans)
    except:
        result = INVALID_REQUEST_PARAMS
    return jsonify(result)


@api.route('/delete/<ip>', methods=['GET'])
def delete_ec2_sync(ip):
    """
    Web handler to delete instance in sync manner
    """
    result = EMPTY_RESPONSE
    try:
        ans = delete_ec2(ip)
        result = make_result_response(ans)
    except:
        result = INVALID_REQUEST_PARAMS
    return jsonify(result)


@api.route('/status/<task_id>', methods=['GET'])
def get_result(task_id):
    """
    Web handler to return the status of async task by task id
    """
    result, status = get_result_from_task_id(async_create_ec2_instance, task_id)
    response = make_result_response(result, status)
    return jsonify(response)


# Running the Flask Server
if __name__ == '__main__':
    api.run(debug=True, host='0.0.0.0')
