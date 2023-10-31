#!/usr/bin/python3

"""Gather data from an API and export it to a JSON file."""

import json
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
            completed_tasks.append({
                "username": employee_name,
                "task": task['title'],
                "completed": task['completed']
            })

        return completed_tasks

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def export_to_json():
    """
    Export completed tasks of all employees to a JSON file.

    Returns:
        None
    """
    all_employees_data = {}
    for employee_id in range(1, 11):  # Assuming 10 employees with IDs from 1 to 10
        completed_tasks = get_employee_todo_progress(employee_id)
        all_employees_data[str(employee_id)] = completed_tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_employees_data, json_file, indent=4)

if __name__ == "__main__":
    export_to_json()
