#!/usr/bin/python3
"""
Script to retrieve and display the titles
of the first 10 hot posts from a specified Reddit subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10
    hot posts for the given subreddit.
    """
    # Construct the URL for the subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Define headers for the HTTP request, including User-Agent
    headers = {
        "User-Agent": "linux:reddit_api_client:v1.0.0 (by /u/your_username)"
    }

    # Define parameters for the request, limiting the number of posts to 10
    params = {
        "limit": 10
    }

    # Send a GET request to the subreddit's hot posts page
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
        )

    # Check if the response status code indicates a not-found error (404)
    if response.status_code == 404:
        print("None")
        return

    # Parse the JSON response and extract the 'data' section
    data = response.json().get("data")

    # Extract the list of posts from the JSON data
    posts = data.get("children")

    # Print the titles of the top 10 hottest posts
    for post in posts:
        print(post.get("data").get("title"))


# Testing the function
if __name__ == "__main__":
    subreddit = input("Enter the name of the subreddit: ")
    top_ten(subreddit)
