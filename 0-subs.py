#!/usr/bin/python3
"""Module that queries the Reddit API and returns subscriber count"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers (not active users) for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers, or 0 if subreddit is invalid.
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Custom User Agent by ALU)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json().get("data", {}).get("subscribers", 0)
        else:
            return 0
    except Exception:
        return 0
