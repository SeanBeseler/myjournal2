"""Views for journal"""
import io
import os
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
from pyramid.httpexceptions import HTTPFound
from myjournal.models import Model_Entry
import datetime
HERE = os.path.dirname(__file__)
Path = os.path.dirname(HERE)

@view_config(route_name='home',  renderer='../templates/index.jinja2')
def list_view(request):
    """Retruns the index.html as the home page"""
    session = request.dbsession
    all_entry = session.query(Model_Entry).order_by(Model_Entry.date).all()
    return {'entry':all_entry}

@view_config(route_name='detail', renderer='../templates/post.jinja2')
def detail_view(request):
        """Retruns the about.html as the detail page"""
        the_id = int(request.matchdict['id'])
        session =request.dbsession
        entry = session.query(Model_Entry).get(the_id)
        if not entry:
             raise HTTPNotFound
        return {'entrys': entry}


@view_config(route_name='create', renderer='../templates/New.jinja2')
def create_view(request):
    """Retruns the new.html as the crate page"""
    if request.method == "GET" :
        return {}
    elif request.method == "POST":
        new_entry = Model_Entry(
            title = request.POST['title'],
            text = request.POST['text'],
            date = datetime.datetime.now().strftime('%m/%d/%y')
        )
        request.dbsession.add(new_entry)
        return HTTPFound( location= request.route_url('home'))


@view_config(route_name='update', renderer='../templates/about.jinja2')
def update_view(request):
    """Retruns the post.html as the update page"""
    the_id = int(request.matchdict['id'])
    session= request.dbsession
    entry = session.query(Model_Entry).get(the_id)
    if not entry:
        raise HTTPNotFound
    if request.method == "GET":
        return{
            "title": entry.title,
            "text":entry.text
        }
    if request.method == "POST":
        entry.title = request.POST['title']
        entry.text = request.POST['text']
        return HTTPFound( location= request.route_url('home'))
    
    return {}
