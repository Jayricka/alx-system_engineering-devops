#!/usr/bin/python3
"""Recursive function to query the Reddit API and return a list containing
the titles of all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = (
        f"https://www.reddit.com/r/{subreddit}/hot.json?"
        f"limit=100&after={after}"
    )
    headers = {"User-Agent": "my-app/0.1.0 (by /u/your_username)"}

    try:
        response = requests.get(
            url, headers=headers, allow_redirects=False
        )
        response.raise_for_status()

        data = response.json().get("data", {}).get("children", [])

        if not data:
            return hot_list

        for post in data:
            hot_list.append(post.get("data", {}).get("title"))

        after = response.json().get("data", {}).get("after")

        return recurse(subreddit, hot_list, after)
    except requests.exceptions.RequestException:
        return None


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
