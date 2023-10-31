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
        dict: Dictionary of completed tasks.
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

        completed_tasks = {str(employee_id): []}
        for task in todos_data:
            completed_tasks[str(employee_id)].append({
                "task": task['title'],
                "completed": task['completed'],
                "username": employee_name
            })

        return completed_tasks

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def export_to_json(employee_id, completed_tasks):
    """
    Export completed tasks to a JSON file.

    Args:
        employee_id (int): The ID of the employee.
        completed_tasks (dict): Dictionary of completed tasks.

    Returns:
        None
    """
    filename = f"{employee_id}.json"

    with open(filename, 'w') as json_file:
        json.dump(completed_tasks, json_file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    completed_tasks = get_employee_todo_progress(employee_id)
    export_to_json(employee_id, completed_tasks)
