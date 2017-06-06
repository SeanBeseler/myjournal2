"""Views for journal"""
import io
import os
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
HERE = os.path.dirname(__file__)
Path = os.path.dirname(HERE)
Entry = [
    {'id':0,'title' :'Sean Beseler', 'date':'6/3/17', 'text':'Pyramid is getting much clearer!'},
    {'id':1,'title' :'Sean Beseler', 'date': '6/1/17', 'text':'To day we started learning how to add a SQL data to our website.'},
    {'id':2,'title' : 'Sean Beseler', 'date': '5/30/17', 'text':'We stared graphs today as well as going over pyramid. I feel that I am way behind in pyramid'},
    {'id':3,'title': 'Sean Beseler', 'date': '5/29/17', 'text': 'To day we had a long code review which did help with the sever project. Thanks for do it.'},
    ]


@view_config(route_name='home',  renderer='../templates/index.jinja2')
def list_view(request):
    """Retruns the index.html as the home page"""
    return {'entry':Entry}

@view_config(route_name='detail', renderer='../templates/post.jinja2')
def detail_view(request):
    """Retruns the about.html as the detail page"""
    try:
        the_id = int(request.matchdict['id'])
        entrys = Entry[the_id]
        return {'entrys': entrys}
    except IndexError:
        raise HTTPNotFound
    

@view_config(route_name='create', renderer='../templates/New.jinja2')
def create_view(request):
    """Retruns the new.html as the crate page"""
    return {}

@view_config(route_name='update', renderer='../templates/about.jinja2')
def update_view(request):
    """Retruns the post.html as the update page"""
    return {}
