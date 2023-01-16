#!/usr/bin/python3
"""Script uses REST API for a given employee to
return information about his/her TODO list progress"""

from csv import writer, QUOTE_ALL
from requests import get
from sys import argv
 
 
if __name__ == "__main__":
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    users = r.json()
    for user in users:
        if user.get('id') == int(argv[1]):
            user_name = user.get('username')
            user_id = user.get('id')
            break

    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = r.json()
    csv_file = str(user_id)+".csv"

    with open(csv_file, mode='w', encoding="UTF8") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            if todo.get('userId') == user_id:
                writer.writerow([
                    user_id,
                    user_name,
                    todo.get('completed'),
                    todo.get('title')
                    ])
