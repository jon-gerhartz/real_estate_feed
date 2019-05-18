import feedparser

links = [
    'https://jerseydigs.com/feed/',
    'https://www.njlux.com/feed/',
]

feed = feedparser.parse(links[0])

import ipdb; ipdb.set_trace()
