#!/usr/bin/python3
"""
this module contains a recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns a list of titles of all hot articles for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    header = {'User-agent': 'Chike'}

    if subreddit is None or type(subreddit) is not str:
        return None

    req = requests.get(url, headers=header, allow_redirects=False).json()
    data = req.get('data')
    if data:
        child = data.get('children')
        for post in child:
            postData = post.get('data')
            title = postData.get('title')
            hot_list.append(title)
        after = data.get('after')

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
