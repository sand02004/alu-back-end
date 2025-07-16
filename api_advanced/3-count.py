#!/usr/bin/python3
"""
This module recursively queries the Reddit API, parses the titles of hot
articles for a given subreddit, and prints the count of specified keywords.
"""

import requests


def count_words(subreddit, word_list, word_count=None, after=None):
    """Recursively counts keywords in the titles of hot Reddit posts"""
    if word_count is None:
        word_count = {}
        word_list = [word.lower() for word in word_list]

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'ALUStudentBot/1.0'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json().get('data', {})
        posts = data.get('children', [])

        for post in posts:
            title_words = post.get('data', {}).get('title', '').lower().split()
            for word in word_list:
                word_count[word] = word_count.get(word, 0) + title_words.count(word)

        after = data.get('after')
        if after is not None:
            return count_words(subreddit, word_list, word_count, after)

        filtered = {k: v for k, v in word_count.items() if v > 0}
        for word, count in sorted(filtered.items(), key=lambda x: (-x[1], x[0])):
            print(f"{word}: {count}")

    except requests.RequestException:
        return
