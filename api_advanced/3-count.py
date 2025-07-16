#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses hot article titles,
and prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, word_dict=None, after=None):
    if word_dict is None:
        word_dict = {}
        word_list = [word.lower() for word in word_list]
        for word in word_list:
            word_dict[word] = 0

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'ALU-RedditProject/1.0'}
    params = {'after': after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get('data', {})
    posts = data.get('children', [])
    after = data.get('after')

    for post in posts:
        title = post['data']['title'].lower().split()
        for word in word_list:
            word_dict[word] += title.count(word)

    if after:
        count_words(subreddit, word_list, word_dict, after)
    else:
        filtered = {k: v for k, v in word_dict.items() if v > 0}
        for word, count in sorted(filtered.items(), key=lambda item: (-item[1], item[0])):
            print(f"{word}: {count}")
