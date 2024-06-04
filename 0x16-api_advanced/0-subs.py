#!/usr/bin/python3
"""
making queries subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Gives the total number of subscribers on the subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    answer = requests.get(url, headers=headers, allow_redirects=False)
    if answer.status_code == 200:
        data = answer.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
