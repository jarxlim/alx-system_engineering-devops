#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API
and prints the titles of the first 10 hot posts listed
"""

import requests


def top_ten(subreddit):
    """prints the titles of first 10 posts listed  given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user_agent = {'User-agent': 'Chike'}

    if subreddit is None or type(subreddit) != str:
        print(None)
    req = requests.get(url, headers=user_agent, allow_redirects=False,
                       params={'limit': 10}).json()
    data = req.get('data')
    if data:
        child = data.get('children')
    if data is not None and child is not None:
        for post in child:
            postData = post.get('data')
            title = postData.get('title')
            print(title)
    else:
        print('None')
