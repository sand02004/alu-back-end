#!/usr/bin/python3
"""Script to gather data from an API and display TODO list progress."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Get user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    employee_name = user_data.get("name")

    # Get user's todos
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    number_done = len(done_tasks)

    # First line of output
    print(f"Employee {employee_name} is done with tasks({number_done}/{total_tasks}):")

    # Print titles of completed tasks
    for task in done_tasks:
        print(f"\t {task.get('title')}")
