
from pyramid import testing
from pyramid.response import Response
#from myjournal.views.default import Entry


def test_home_view_returns_response():
    """checks the returns response for home"""
    from myjournal.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)
    assert isinstance(response, Response)


def test_creat_view_returns_response():
    """check the returns response for creat"""
    from myjournal.views.default import create_view
    request = testing.DummyRequest()
    response = create_view(request)
    assert isinstance(response, Response)


def test_home_view_returns_good():
    """check the status code for home"""
    from myjournal.views.default import list_view
    request = testing.DummyRequest()
    response = list_view(request)
    assert response.status_code == 200


def test_creat_view_returns_good():
    """check the status code for creat"""
    from myjournal.views.default import create_view
    request = testing.DummyRequest()
    response = create_view(request)
    assert response.status_code == 200
