#!/usr/bin/python3
"""
0-subs
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers. If the subreddit is not valid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    headers = {'User-Agent': 'CustomUserAgent/1.0'}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json().get('data', {}).get('subscribers', 0)
    elif response.status_code == 404:
        return 0
    else:
        print(f"Error: {response.status_code}")
        return 0

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
