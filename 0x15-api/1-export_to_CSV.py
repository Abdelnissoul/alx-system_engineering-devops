#!/usr/bin/python3
""" 
Export employee TODO list progress to CSV format.
"""

import csv
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    # Fetch user data
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"User with ID {employee_id} not found.")
        sys.exit(1)
    user_data = user_response.json()
    username = user_data.get('username')

    # Fetch tasks data
    tasks_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    tasks_response = requests.get(tasks_url)
    tasks = tasks_response.json()

    # Write to CSV file
    csv_filename = f'{employee_id}.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            csvwriter.writerow([
                employee_id,
                username,
                task.get('completed'),
                task.get('title')
            ])
