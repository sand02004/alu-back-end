#!/usr/bin/python3
"""Gather data from an API and display TODO list progress of an employee"""
import requests
import sys

if __name__ == "__main__":
    try:
        employee_id = int(sys.argv[1])
    except (IndexError, ValueError):
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Get employee info
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_res = requests.get(user_url)
    if user_res.status_code != 200:
        print("Employee not found")
        sys.exit(1)

    user = user_res.json()
    employee_name = user.get("name")

    # Get employee's todos
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_res = requests.get(todos_url)
    todos = todos_res.json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]
    number_done = len(done_tasks)

    # Print required format
    print(f"Employee {employee_name} is done with tasks({number_done}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")
