#!/usr/bin/python3
"""REST API for todo lists of employees"""

import requests
import sys import argv


if __name__ == '__main__':
    employeeId = argv[1]
    employee = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(employeeId), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(employeeId), verify=False).json()

    done_tasks = []
    for task in todo:
        if task.get('completed') is True:
            done_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(done_tasks), len(todo)))

    for task in done_tasks:
        print("\t {}".format(task))
