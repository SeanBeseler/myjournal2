import os
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Everyone, Authenticated, Allow
from passlib.apps import custom_app_context as context
from pyramid.session import SignedCookieSessionFactory

class MyRoot(object):
    def __init__(self,request):
        self.request=request
    __acl__=[(Allow, Authenticated, 'secret')]
def check_credentials(username, password):
    """checks credentials of new user.
        Return True if it checks out: otherwise return False"""
    stored_username = os.environ.get('AUTH_USERNAME','')
    stored_password = os.environ.get('AUTH_PASSWORD','')
    if stored_password and stored_username:
        if context.verify(password,stored_password) and username == stored_username:
            return True
    return False

def includeme(config):
    import pdb; pdb.set_trace()
    auth_secret = os.environ.get('AUTH_SECRET','')
    authn_policy = AuthTktAuthenticationPolicy( secret=auth_secret, hashalg='sha512')
    config.set_authentication_policy(authn_policy)
    authz_policy = ACLAuthorizationPolicy()
    config.set_authorization_policy(authz_policy)
    config.set_root_factory(MyRoot)
    # session_secret = os.environ.get('SESSION_SECRET')
    # session_factory=SignedCookieSessionFactory(session_secret)
    # config.set_session_factory(session_factory)
