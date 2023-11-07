#!/usr/bin/python3
"""
this module functions in returning the number of subscribers for reddit
"""

import requests


def number_of_subscribers(subreddit):
    """function returns the number of subscribers for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user_agent = {'User-agent': 'Chike'}
    request = requests.get(url, headers=user_agent, allow_redirects=False)
    if request.status_code == 200:
        request = request.json()
        data = request.get('data')
        subs = data.get('subscribers')
        return subs
    return 0
