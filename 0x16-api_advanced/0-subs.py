#!/usr/bin/python3
"""
Query the number of subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers for the subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data.get("data", {}).get("subscribers", 0)
        return subscribers
    else:
        return 0


# Test the function
if __name__ == "__main__":
    subreddit = input("Enter the name of the subreddit: ")
    subscribers = number_of_subscribers(subreddit)
    print(f"The number of subscribers on r/{subreddit}: {subscribers}")
