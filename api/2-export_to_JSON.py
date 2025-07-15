#!/usr/bin/python3
"""Exports an employee's TODO list to JSON format"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Get user info
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_res = requests.get(user_url)
    user = user_res.json()
    username = user.get("username")

    # Get todos
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_res = requests.get(todos_url)
    todos = todos_res.json()

    # Create list of task dicts
    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    # Create final JSON data
    data = {employee_id: tasks}

    # Export to file
    filename = f"{employee_id}.json"
    with open(filename, "w") as json_file:
        json.dump(data, json_file)
