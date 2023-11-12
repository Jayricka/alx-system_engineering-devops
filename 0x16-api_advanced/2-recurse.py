#!/usr/bin/python3
"""
recursive function to query Reddit API for hot articles in a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after, 'limit': 100}
    headers = {'User-Agent': 'your_user_agent'}
    response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    if not data or 'children' not in data:
        return hot_list

    children = data['children']
    titles = [child.get('data', {}).get('title', '') for child in children]
    hot_list.extend(titles)

    after = data.get('after')
    return recurse(subreddit, hot_list, after)


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result:
            print(len(result))
        else:
            print("None")
