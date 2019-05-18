"""
Real Estate Blog Links
    [blog_site1, blog_site2, ...]

Real Estate Blog Data Model

    id: int
        author: string
        url: string
        title: string
        date: datetime
        summary: string
        tags: [tag1, tag2, ...]

Real Estate Agent Data Model

    id: int
        name: string
        email: string    


Emails Data Model

    id: int
        agent_id: int
        time_sent: datetime
        blog_ids: [int, ...]
"""

from datetime import datetime

blog_links = [
    'https://jerseydigs.com/feed/',
    'https://www.njlux.com/feed/',
]

blog_data = {}

agent_data = {
    'id': 1,
    'name': 'Mitchell Bregman',
    'email': 'mitchbregs@gmail.com'
}

email_data = {}


def _get_blog_links():
    return blog_links


def _get_blog_data(id):
    return blog_data[id]


def _get_agent_data(id):
    return agent_data[id]


def _get_email_data(id):
    return email_data[id]


def _add_blog_links(link):
    blog_links.append(link)


def _add_blog_data(url, author, title, date, summary, tags):
    id = len(blog_data) + 1
    blog_data[id] = {
        'url': url,
        'author': author,
        'title': title,
        'date': date,
        'summary': summary,
        'tags': tags
    }


def _add_agent_data(name, email):
    id = len(agent_data) + 1 
    agent_data[id] = { 
        'name': name,
        'email': email
    }  


def _add_email_data(agent, date, blog_ids):
    id = len(email_data) + 1 
    email_data[id] = { 
        'agent': agent,
        'date': date,
        'blogs': blog_ids
    }  
