#!/usr/bin/python3
"""
Gather employee TODO list progress from API.
"""

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"


def fetch_employee_todo_progress(employee_id):
    """
    Fetches and prints the TODO list progress of an employee.
    """
    # Get employee information
    user_url = f"{REST_API}/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee not found")
        return

    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Get TODO list for the employee
    todos_url = f"{REST_API}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Filter tasks for the given employee
    tasks = [task for task in todos_data if task.get('userId') == employee_id]
    completed_tasks = [task for task in tasks if task.get('completed')]

    # Print the results
    print(
        f"Employee {employee_name} is done with tasks"
        f"({len(completed_tasks)}/{len(tasks)}):"
    )
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    if not re.fullmatch(r'\d+', sys.argv[1]):
        print("Employee ID must be an integer")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)
