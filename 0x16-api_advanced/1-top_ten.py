#!/usr/bin/python3
"""query titles of first 10 hot posts for a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "my-app/0.1.0 (by /u/ricka)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        data = response.json().get("data", {}).get("children", [])
        for post in data:
            print(post.get("data", {}).get("title"))
    except requests.exceptions.RequestException:
        print(None)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
