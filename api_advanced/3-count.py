#!/usr/bin/python3
"""Recursive function to count words in hot Reddit posts"""
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """Counts keywords recursively in the titles of hot posts"""
    if after is None:
        word_count = {}
        word_list = [word.lower() for word in word_list]

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'ALUStudentBot/1.0'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json().get('data', {})
        posts = data.get('children', [])

        for post in posts:
            title_words = post.get('data', {}).get('title', '').lower().split()
            for word in word_list:
                count = title_words.count(word)
                if count > 0:
                    word_count[word] = word_count.get(word, 0) + count

        # Check if there's another page
        after = data.get('after')
        if after is not None:
            return count_words(subreddit, word_list, word_count, after)

        # Done: print the results
        if word_count:
            for word in sorted(word_count.items(), key=lambda item: (-item[1], item[0])):
                print(f"{word[0]}: {word[1]}")

    except requests.RequestException:
        return
