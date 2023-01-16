#!/usr/bin/python3
"""Script uses REST API for a given employee to
return information about his/her TODO list progress
and exports data to json
"""
import json
import requests
from sys import argv


BASE_URL = 'https://jsonplaceholder.typicode.com'

user = requests.get(f'{BASE_URL}/users/{argv[1]}').json()
todos = requests.get(f'{BASE_URL}/todos', params={"userId": argv[1]}).json()

with open(f'{argv[1]}.json', 'w', encoding='utf8') as f:
    tasks = []
    for todo in todos:
        tasks.append({"task": f'{todo["title"]}',
                      "completed": f'{str(todo["completed"])}',
                      "username": f'{user["name"]}'})
    data = {f"{argv[1]}": tasks}
    json_string = json.dumps(data)
    f.write(json_string.rstrip())
