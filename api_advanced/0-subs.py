#!/usr/bin/python3
"""Module for querying subreddit subscriber count using Reddit API"""

import requests


# Defining number of subscribers
def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    if not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'ALUStudentBot/1.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json().get('data', {}).get('subscribers', 0)
        return 0
    except requests.RequestException:
        return 0
