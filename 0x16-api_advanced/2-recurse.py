#!/usr/bin/python3
"""2-recurse - Recursive fetches all hot post titles for a subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Fetches all hot post titles recursively for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'python:recurse:v1.0 (by /u/your_username)'
    }
    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        if response.status_code == 200:
            data = response.json()
            posts = data.get("data", {}).get("children", [])
            for post in posts:
                hot_list.append(post.get("data", {}).get("title"))

            after = data.get("data", {}).get("after")

            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list if hot_list else None
        else:
            return None
    except Exception:
        return None
