#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flake8: noqa
from celery import Celery
import os
import crypt
import json


app = Celery('tasks', backend='redis://localhost', broker='redis://localhost:6379/0')
KEY = 'guest'


def _spawn_ec2_instance(username, password):
    """
    Spawn a EC2 Instance using Ansible and return public IP of Instance
    """
    encrypted_password = crypt.crypt(password, KEY)
    command = 'ansible-playbook -e "user=%s password=%s" create-instance.yml' % (username, encrypted_password)
    print "***************"
    print command
    print "***************"
    response = os.popen(command).read()
    aws_cmd = 'aws ec2 describe-instances --filters "Name=tag:Name,Values=suite" "Name=tag:User,Values=%s" "Name=instance-state-name,Values=running"' % (username)
    info = os.popen(aws_cmd).read()
    ec2_info = json.loads(info)
    instance_ip = ec2_info['Reservations'][0]['Instances'][0]['PublicIpAddress']
    return instance_ip


def _delete_ec2_instance(ip):
    """
    Delete an existing EC2 instance by its public IP
    """
    aws_cmd = 'aws ec2 describe-instances --filters "Name=ip-address,Values=%s"' % (ip)
    info = os.popen(aws_cmd).read()
    ec2_info = json.loads(info)
    try:
        instance_id = ec2_info['Reservations'][0]['Instances'][0]['InstanceId']
        command = 'ansible-playbook -e "id=%s" delete-instance.yml' % (instance_id)
        print "#################"
        print command
        print "#################"
        response = os.popen(command)
        return ip
    except:
        return 'Instance with ip %s not found!' % (ip)


@app.task
def async_create_ec2_instance(username, password):
    """
    Running ansible playbook to trigger ec2 instance in async manner
    """
    return _spawn_ec2_instance(username, password)


def create_ec2_instance(username, password):
    """
    Running ansible playbook to trigger ec2 instance in sync manner
    """
    return _spawn_ec2_instance(username, password)


def delete_ec2(ip):
    """
    Running ansible playbook to delete EC2 instance in sync manner
    """
    return _delete_ec2_instance(ip)

@app.task
def async_delete_ec2(ip):
    """
    Running ansible playbook to delete EC2 instance in async manner
    """
    return _delete_ec2_instance(ip)
