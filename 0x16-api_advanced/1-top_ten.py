#!/usr/bin/python3
"""1-top_ten"""

import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'CustomUserAgent/1.0'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        [print(post.get('data', {}).get('title')) for post in response.json().get('data', {}).get('children', [])]
    elif response.status_code == 404:
        print(None)
    else:
        print(f"Error: {response.status_code}")
        print(None)

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
