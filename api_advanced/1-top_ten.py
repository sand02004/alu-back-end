#!/usr/bin/python3
"""Module for printing the titles of the first 10 hot posts in a subreddit"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit"""
    if not isinstance(subreddit, str):
        print(None)
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'ALUStudentBot/1.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            print(None)
            return

        posts = response.json().get('data', {}).get('children', [])

        for post in posts:
            print(post.get('data', {}).get('title'))
    except requests.RequestException:
        print(None)
