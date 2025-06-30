#!/usr/bin/python3
"""Exports data for a given employee ID to a CSV file"""

import csv
import requests
import sys

if __name__ == "__main__":
        user_id = sys.argv[1]

            # Get user information
                user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
                    user = requests.get(user_url).json()
                        username = user.get("username")

                            # Get user's todo list
                                todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
                                    todos = requests.get(todos_url).json()

                                        # Create CSV file
                                            filename = f"{user_id}.csv"
                                                with open(filename, "w", newline="") as csvfile:
                                                            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
                                                                    for task in todos:
                                                                                    writer.writerow([
                                                                                                        user_id,
                                                                                                                        username,
                                                                                                                                        task.get("completed"),
                                                                                                                                                        task.get("title")
                                                                                                                                                                    ])

