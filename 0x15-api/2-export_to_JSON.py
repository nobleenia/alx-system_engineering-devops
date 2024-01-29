#!/usr/bin/python3
"""
Script that, uses a REST API,
for a given employee ID,
Returns information about his/her TODO list progress,
exporting data in JSON format
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    sessionReq = requests.Session()

    idEmp = argv[1]
    idURL = "https://jsonplaceholder.typicode.com/users/{}/todos".format(idEmp)
    nameURL = "https://jsonplaceholder.typicode.com/users/{}".format(idEmp)

    employee = sessionReq.get(idURL)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    name = employeeName.json()['username']

    totalTasks = []
    updateUser = {}

    for all_Emp in json_req:
        totalTasks.append(
            {
                "task": all_Emp.get('title'),
                "completed": all_Emp.get('completed'),
                "username": name,
                })
        updateUser[idEmp] = totalTasks

        file_Json = idEmp + ".json"
        with open(file_Json, "w") as f:
            json.dump(updateUser, f)
