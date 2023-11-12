#!/usr/bin/python3
"""
100-count
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    if after is None:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'

    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        )
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])

        if not children:
            return

        for child in children:
            title = child.get('data', {}).get('title', '').lower()
            for word in word_list:
                word_lower = word.lower()
                counts[word_lower] = (
                    counts.get(word_lower, 0) +
                    title.count(word_lower)
                )

        after = data.get('after', None)
        if after:
            count_words(subreddit, word_list, after, counts)
        else:
            print_results(counts)

    elif response.status_code == 404:
        pass  # Do nothing for invalid subreddit

    else:
        pass  # Do nothing for other errors


def print_results(counts):
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        if count > 0:
            print(f"{word}: {count}")


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <subreddit> <list of keywords>")
        print(f"Ex: {sys.argv[0]} programming 'python java javascript'")
    else:
        result = count_words(sys.argv[1], [x for x in sys.argv[2].split()])
