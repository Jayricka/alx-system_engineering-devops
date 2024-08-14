#!/usr/bin/python3
"""100-count - Recursively counts keywords in titles of hot posts."""
import requests
import re


def count_words(subreddit, word_list, counts=None, after=None):
    """Counts occurrences of keywords in hot post titles recursively."""
    if counts is None:
        counts = {word.lower(): 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'python:count_words:v1.0 (by /u/your_username)'
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
                title = post.get("data", {}).get("title", "").lower()
                for word in counts:
                    word_pattern = rf'\b{re.escape(word)}\b'
                    counts[word] += len(re.findall(word_pattern, title))

            after = data.get("data", {}).get("after")
            if after is not None:
                return count_words(subreddit, word_list, counts, after)
            else:
                sorted_counts = sorted(
                    ((word, count) for word, count in counts.items()
                     if count > 0),
                    key=lambda x: (-x[1], x[0])
                )
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
                return
        else:
            return
    except Exception:
        return
