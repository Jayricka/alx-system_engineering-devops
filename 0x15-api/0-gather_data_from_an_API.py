#!/usr/bin/python3
"""Gather data from an API and display employee's TODO list progress."""

import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Retrieve and display an employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
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

        employee_name = user_data['name']

        total_tasks = len(todos_data)
        completed_tasks = sum(1 for task in todos_data if task['completed'])
        completed_task_titles = [task['title'] for task in todos_data if task['completed']]  # Fixed the missing bracket here.

        print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
        for title in completed_task_titles:
            print(f"\t{title}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
