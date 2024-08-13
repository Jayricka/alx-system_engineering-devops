#!/usr/bin/python3
"""
0-subs - Fetches the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Fetches the number of subscribers for a subreddit.
    Parameters:
    subreddit (str): The name of the subreddit.
    Returns:
    int: Number of subscribers or 0 if subreddit is invalid.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        'User-Agent': 'myapi/0.0.1 (contact: myemail@example.com)'
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        return 0
    except requests.RequestException:
        return 0
