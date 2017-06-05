"""Views for journal"""
import io
import os
from pyramid.response import Response
HERE = os.path.dirname(__file__)
Path = os.path.dirname(HERE)
NPath = os.path.join(Path, 'templates', 'index.html')
EPath = os.path.join(Path, 'templates', 'post.html')
SPath = os.path.join(Path, 'templates', 'New.html')
WPath = os.path.join(Path,'templates', 'about.html')
def list_view(request):
    """Retruns the index.html as the home page"""
    with io.open(NPath) as the_file:
        imported_text = the_file.read()
    return Response(imported_text)

def detail_view(request):
    """Retruns the about.html as the home page"""
    with io.open(EPath) as the_file:
        imported_text = the_file.read()
    return Response(imported_text)

def create_view(request):
    """Retruns the new.html as the home page"""
    with io.open(SPath) as the_file:
        imported_text = the_file.read()
    return Response(imported_text)

def update_view(request):
    """Retruns the post.html as the home page"""
    with io.open(WPath) as the_file:
        imported_text = the_file.read()
    return Response(imported_text)
