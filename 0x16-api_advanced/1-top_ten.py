#!/usr/bin/python3
"""1-top_ten - Fetches prints top 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Fetch print titles of the first 10 hot posts for a subreddit."""
    url = (
        f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    )
    headers = {
        'User-Agent': 'python:top_ten:v1.0 (by /u/your_username)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get("data", {}).get("children", [])
            for post in posts:
                print(post.get("data", {}).get("title"))
        else:
            print(None)
    except Exception:
        print(None)
