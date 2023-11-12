#!/usr/bin/python3
"""
This module defines a recursive function to query the Reddit API and count occurrences of keywords in hot articles.
"""

import requests
import time


def count_words(subreddit, word_list, after=None, counts=None, retries=3):
    if counts is None:
        counts = {}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after, 'limit': 100}
    headers = {'User-Agent': 'your_user_agent'}
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 429 and retries > 0:
        print(f"Rate limited. Retrying in 5 seconds... ({retries} retries left)")
        time.sleep(5)
        return count_words(subreddit, word_list, after, counts, retries - 1)

    if response.status_code != 200:
        print(f"Failed to retrieve data from Reddit API. Status code: {response.status_code}")
        return counts

    data = response.json().get('data', {})
    if not data or 'children' not in data:
        print("No data or 'children' key in the API response.")
        return counts

    children = data['children']
    titles = [child.get('data', {}).get('title', '') for child in children]

    for word in word_list:
        word = word.lower()
        count = sum(title.lower().count(word) for title in titles)
        counts[word] = counts.get(word, 0) + count

    after = data.get('after')
    return count_words(subreddit, word_list, after, counts)


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <subreddit> <list of keywords>")
        print(f"Example: {sys.argv[0]} programming 'python java javascript'")
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2].split()
        result = count_words(subreddit, word_list)

        if not result:
            print("No matches found.")
        else:
            sorted_counts = sorted(result.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
