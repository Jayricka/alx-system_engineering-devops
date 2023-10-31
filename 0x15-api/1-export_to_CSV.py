#!/usr/bin/python3

"""Export data from an API to a CSV file."""

import csv
import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Retrieve an employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        list: List of completed tasks.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)
        user_data = user_response.json()
        todos_data = todos_response.json()

        if user_response.status_code != 200:
            print("User not found")
            sys.exit(1)

        employee_id = user_data['id']
        employee_name = user_data['username']

        completed_tasks = []
        for task in todos_data:
            completed_tasks.append([str(employee_id), employee_name, str(task['completed']), task['title']])

        return completed_tasks

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def export_to_csv(employee_id, completed_tasks):
    """
    Export completed tasks to a CSV file.

    Args:
        employee_id (int): The ID of the employee.
        completed_tasks (list): List of completed tasks.

    Returns:
        None
    """
    filename = f"{employee_id}.csv"

    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        writer.writerows(completed_tasks)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    completed_tasks = get_employee_todo_progress(employee_id)
    export_to_csv(employee_id, completed_tasks)
