#!/usr/bin/python3
"""
Script that, uses a REST API,
for a given employee ID,
Returns information about his/her TODO list progress,
exporting data in CSV format
"""
import csv
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

    totalTasks = 0

    for done_tasks injson_req:
        if done_rasks['complted']:
            totalTasks += 1

    CSVfile = idEmp + ".csv"

    with open(CSVfile, "w", newline="") as csvfile:
        write = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_ALL)
        for i in json_req:
            write.writerow([idEmp, name, i.get('completed'), i.get('title')])
