#!/usr/bin/python3
"""REST API for todo lists of employees"""
import csv
import json
import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(user_id), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(user_id), verify=False).json()

    username = user.get('username')
    tasks = []
    for task in todo:
        dictionary = {}
        dictionary["task"] = task.get('title')
        dictionary["completed"] = task.get('completed')
        dictionary["username"] = username
        tasks.append(dictionary)

    JsonObj = {}
    JsonObj[user_id] = tasks
    with open("{}.json".format(user_id), 'w') as jsonfile:
        json.dump(JsonObj, jsonfile)
