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
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    todoAll = {}

    for user in users:
        task_list = []
        for task in todos:
            if task.get("userId") == user.get("id"):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                task_list.append(taskDict)
        todoAll[user.get('id')] = task_list

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todoAll, f)
