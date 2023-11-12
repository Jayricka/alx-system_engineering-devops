#!/usr/bin/python3
"""
query the Reddit API for hot articles in a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    if not is_valid_subreddit(subreddit):
        return None

    if hot_list is None:
        hot_list = []

    if after is None:
        return hot_list

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after, 'limit': 100}
    headers = {'User-Agent': 'your_user_agent'}
    response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        return None

    data = response.json()
    children = data.get('data', {}).get('children', [])
    titles = [child.get('data', {}).get('title', '') for child in children]
    hot_list.extend(titles)

    after = data.get('data', {}).get('after')
    return recurse(subreddit, hot_list, after)


def is_valid_subreddit(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'your_user_agent'}
    response = requests.get(url, headers=headers)
    return (
        response.status_code == 200
        and response.json().get('data', {}).get('display_name') == subreddit
    )


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
