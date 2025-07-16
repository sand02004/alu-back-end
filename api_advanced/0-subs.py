#!/usr/bin/python3
""" Function that returns the number of subscribers for a subreddit """
import requests


def number_of_subscribers(subreddit):
    """Returns total number of subscribers for a given subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'ALUStudentBot/1.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception:
        return 0
