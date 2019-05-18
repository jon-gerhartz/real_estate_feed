import feedparser

from data import data_models as model

feed = feedparser.parse(model.blog_links[0])

"""
1) Break down the feed model; append feed model data to data_model. This will eventually turn into a database or JSON; temporary.
2) Take data_model data; turn into human readable HTML form.
3) For every agent in agent data_model, send HTML of RSS along with agent name, picture, etc.
"""

"""
Link 1: Response - Example:

    {'author': 'Gillian Blair',
 'author_detail': {'name': 'Gillian Blair'},
 'authors': [{'name': 'Gillian Blair'}],
 'guidislink': False,
 'id': 'http://jerseydigs.com/?p=24817',
 'link': 'https://jerseydigs.com/five-new-construction-condos-for-sale-385-eighth-street-jersey-city/',
 'links': [{'href': 'https://jerseydigs.com/five-new-construction-condos-for-sale-385-eighth-street-jersey-city/',
            'rel': 'alternate',
            'type': 'text/html'}],
 'published': 'Fri, 17 May 2019 14:10:26 +0000',
 'published_parsed': time.struct_time(tm_year=2019, tm_mon=5, tm_mday=17, tm_hour=14, tm_min=10, tm_sec=26, tm_wday=4, tm_yday=137, tm_isdst=0),
 'summary': '<p>385 8th Street brings Soho-style digs with outdoor space to '
            'Downtown Jersey City near Hamilton Park.</p>\n'
            '<p>The post <a rel="nofollow" '
            'href="https://jerseydigs.com/five-new-construction-condos-for-sale-385-eighth-street-jersey-city/">New '
            'Construction Condos For Sale in Lofty Eighth Street Building</a> '
            'appeared first on <a rel="nofollow" '
            'href="https://jerseydigs.com">Jersey Digs</a>.</p>',
 'summary_detail': {'base': 'https://jerseydigs.com/feed/',
                    'language': None,
                    'type': 'text/html',
                    'value': '<p>385 8th Street brings Soho-style digs with '
                             'outdoor space to Downtown Jersey City near '
                             'Hamilton Park.</p>\n'
                             '<p>The post <a rel="nofollow" '
                             'href="https://jerseydigs.com/five-new-construction-condos-for-sale-385-eighth-street-jersey-city/">New '
                             'Construction Condos For Sale in Lofty Eighth '
                             'Street Building</a> appeared first on <a '
                             'rel="nofollow" '
                             'href="https://jerseydigs.com">Jersey '
                             'Digs</a>.</p>'},
 'tags': [{'label': None, 'scheme': None, 'term': 'Jersey City'},
          {'label': None, 'scheme': None, 'term': 'Listing'},
          {'label': None, 'scheme': None, 'term': 'Sponsored'},
          {'label': None, 'scheme': None, 'term': '385 8th Street'}],
 'title': 'New Construction Condos For Sale in Lofty Eighth Street Building',
 'title_detail': {'base': 'https://jerseydigs.com/feed/',
                  'language': None,
                  'type': 'text/plain',
                  'value': 'New Construction Condos For Sale in Lofty Eighth '
                           'Street Building'}}


"""

for i in range(0, len(feed['entries'])):
    # *** TypeError: _add_blog_data() missing 6 required positional arguments: 'url', 'author', 'title', 'date', 'summary', and 'tags'
    model._add_blog_data(
        url = feed['entries'][i]['link'],
        author = feed['entries'][i]['author'],
        title = feed['entries'][i]['title'],
        date = feed['entries'][i]['published'],
        summary = feed['entries'][i]['summary'],
        tags = [tag['term'] for tag in feed['entries'][i]['tags']] 
    )

import ipdb; ipdb.set_trace()
