#!/usr/bin/python3
"""
Requests module for sending HTTP requests to the Reddit API
"""
import requests


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit"""

    headers = {'User-Agent': 'MyRedditBot/0.0.1'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    request = requests.get(url, headers=headers, allow_redirects=False)
    if (request.status_code == 200):
        posts = request.json()['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
